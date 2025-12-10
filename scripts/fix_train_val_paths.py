import os

# Change only these paths ↓↓↓
base_path = r"D:/Deep Learning/pbl project/idd_dataset/IDD_Detection/JPEGImages"

train_input = r"D:/Deep Learning/pbl project/idd_dataset/IDD_Detection/train.txt"
val_input = r"D:/Deep Learning/pbl project/idd_dataset/IDD_Detection/val.txt"

train_output = r"D:/Deep Learning/pbl project/idd_dataset/IDD_Detection/train_fixed.txt"
val_output = r"D:/Deep Learning/pbl project/idd_dataset/IDD_Detection/val_fixed.txt"

test_input = r"D:/Deep Learning/pbl project/idd_dataset/IDD_Detection/test.txt"
test_output = r"D:/Deep Learning/pbl project/idd_dataset/IDD_Detection/test_fixed.txt"


def fix_paths(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.read().splitlines()

    with open(output_file, "w") as f:
        for line in lines:
            full_path = os.path.join(base_path, line + ".jpg")
            f.write(full_path.replace("\\", "/") + "\n")
    print(f"✅ Saved: {output_file}")



fix_paths(train_input, train_output)
fix_paths(val_input, val_output)
fix_paths(test_input, test_output)
