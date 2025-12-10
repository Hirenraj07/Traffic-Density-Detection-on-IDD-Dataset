# Traffic-Density-Detection-on-IDD-Dataset
Built an end-to-end traffic object detection pipeline by fine-tuning YOLOv8 on the IDD (IIIT-Hyderabad) dataset. Implemented dataset conversion (XML→YOLO), automated splitting, custom training in Google Colab, and robust inference workflows. The model detects multiple vehicle and road-user classes to support traffic density estimation and analysis.

# IDD Traffic Detection — YOLOv8 Fine-tuning

**project summary:** Fine-tuned YOLOv8 on the IDD (IIIT-Hyderabad) dataset for robust road-user detection and traffic-density estimation.

**Dataset:** IDD (IIIT-H) — used images & annotations from the IDD Detection split. Source: https://idd.insaan.iiit.ac.in/dataset/details/

---

## Repo contents
- `notebooks/` — Colab notebooks (data prep, training, inference).
- `scripts/` — scripts to convert annotations, split dataset, train and run inference.
- `configs/` — training configs and hyperparameters.
- `assets/` — demo images/GIFs and visual results.
- `runs/` — **not** tracked (models and logs stored in Drive or Releases).
---

## Colab Project Structure: https://drive.google.com/drive/folders/1kpaHpU4c9I4S_4b3aaixmsJf8PEl1fTx?usp=sharing

##  Quick start (Colab)
1. Mount Drive and clone repo to `/content/drive/MyDrive/...` (or clone locally).
2. Install dependencies:
```bash
pip install -r requirements.txt

python scripts/train_finetune.py --data idd.yaml --weights /path/to/weights.pt --epochs 30
python scripts/infer.py --weights /path/to/best.pt --img /path/to/sample.jpg --save


