import os
import xml.etree.ElementTree as ET
from concurrent.futures import ProcessPoolExecutor, as_completed

# ====== CONFIGURE THESE PATHS ======
INPUT_DIR = r"D:\Deep Learning\pbl project\idd_dataset\IDD_Detection\Annotations"
OUTPUT_DIR = r"D:\Deep Learning\pbl project\idd_dataset\IDD_Detection\labels"

# Class names (must match your dataset)
CLASSES = [
    "car",
    "person",
    "motorcycle",
    "autorickshaw",
    "truck",
    "bus",
    "bicycle",
    "animal",
    "traffic sign",
    "traffic light",
    "vehicle fallback",
    "curb",
    "guard rail",
    "road",
    "sidewalk",
    "building",
    "wall",
    "fence",
    "pole",
    "vegetation",
    "sky",
    "terrain",
    "ego vehicle"
]

def convert_bbox(size, box):
    """Convert VOC bbox (xmin, xmax, ymin, ymax) to YOLO (x_center, y_center, w, h)."""
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x *= dw
    w *= dw
    y *= dh
    h *= dh
    return (x, y, w, h)


def process_xml(xml_path):
    """Convert one XML file to YOLO format."""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        size_elem = root.find("size")
        if size_elem is None:
            return  # skip if image size is missing
        w = int(size_elem.find("width").text)
        h = int(size_elem.find("height").text)

        label_lines = []
        for obj in root.findall("object"):
            cls = obj.find("name").text.strip()
            if cls not in CLASSES:
                continue
            cls_id = CLASSES.index(cls)
            xmlbox = obj.find("bndbox")
            b = (
                float(xmlbox.find("xmin").text),
                float(xmlbox.find("xmax").text),
                float(xmlbox.find("ymin").text),
                float(xmlbox.find("ymax").text),
            )
            bb = convert_bbox((w, h), b)
            label_lines.append(f"{cls_id} {' '.join(map(str, bb))}")

        if label_lines:
            rel_path = os.path.relpath(xml_path, INPUT_DIR)
            save_dir = os.path.join(OUTPUT_DIR, os.path.dirname(rel_path))
            os.makedirs(save_dir, exist_ok=True)
            save_path = os.path.join(save_dir, os.path.basename(xml_path).replace(".xml", ".txt"))
            with open(save_path, "w") as f:
                f.write("\n".join(label_lines))

    except Exception as e:
        print(f"❌ Error processing {xml_path}: {e}")


if __name__ == "__main__":
    # Windows-safe multiprocessing start
    print("🔍 Scanning annotation folders...")

    xml_files = []
    for root, _, files in os.walk(INPUT_DIR):
        for file in files:
            if file.endswith(".xml"):
                xml_files.append(os.path.join(root, file))

    print(f"📁 Found {len(xml_files)} XML files. Starting conversion using multiprocessing...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Adjust worker count if needed (default: all cores)
    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_xml, xml): xml for xml in xml_files}
        for i, future in enumerate(as_completed(futures), 1):
            xml = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"⚠️ Error in {xml}: {e}")
            if i % 1000 == 0:
                print(f"✅ Processed {i}/{len(xml_files)} files...")

    print("🎯 Conversion complete! Check your 'labels' folder.")
