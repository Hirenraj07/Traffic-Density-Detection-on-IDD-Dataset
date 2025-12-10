import os

label_root = r"D:\Deep Learning\pbl project\idd_dataset\IDD_Detection\labels"

# Count how many .txt labels exist and preview a few paths
count = 0
for root, _, files in os.walk(label_root):
    for f in files:
        if f.endswith(".txt"):
            count += 1
            if count <= 5:
                print(os.path.join(root, f))

print(f"\n✅ Total YOLO label files found: {count}")
