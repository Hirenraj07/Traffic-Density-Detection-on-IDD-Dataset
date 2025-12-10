import os, random, shutil

# Base paths
base_dir = r"D:\Deep Learning\pbl project\IDD_Detection"
img_dir = os.path.join(base_dir, "images")
lbl_dir = os.path.join(base_dir, "labels")

# Create split folders if not present
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(img_dir, split), exist_ok=True)
    os.makedirs(os.path.join(lbl_dir, split), exist_ok=True)

# Get list of all images
images = [f for f in os.listdir(img_dir) if f.endswith(".jpg") or f.endswith(".png")]
random.shuffle(images)

n = len(images)
train_end = int(n * 0.8)
val_end = int(n * 0.9)

print(f"Total images found: {n}")
print("Splitting into:")
print(f" - Train: {train_end}")
print(f" - Val: {val_end - train_end}")
print(f" - Test: {n - val_end}")

# Move files
for i, img_name in enumerate(images):
    if i < train_end:
        split = "train"
    elif i < val_end:
        split = "val"
    else:
        split = "test"

    label_name = os.path.splitext(img_name)[0] + ".txt"

    src_img = os.path.join(img_dir, img_name)
    dst_img = os.path.join(img_dir, split, img_name)

    src_lbl = os.path.join(lbl_dir, label_name)
    dst_lbl = os.path.join(lbl_dir, split, label_name)

    try:
        shutil.move(src_img, dst_img)
        if os.path.exists(src_lbl):
            shutil.move(src_lbl, dst_lbl)
    except Exception as e:
        print(f"Error moving {img_name}: {e}")

    if i % 1000 == 0:
        print(f"{i}/{n} files processed...")

print("\n✅ Dataset split completed successfully!")
