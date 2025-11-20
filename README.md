# Project-Moody-s

Tensor-network based methods for option pricing (Semester Project, Moody's / ETH).

This repository contains personal workspaces for each team member.  
Each person develops and experiments inside their own folder, mainly using Jupyter notebooks.

---

## Repository structure

```
BiagiBoss/       # Biagi's code and notebooks
CortoBoss/       # Corto's code and notebooks
PalumboBoss/     # Alessandro's code and notebooks
SanninoBoss/     # Sannino's code and notebooks
main/            # shared code (if we ever need common utilities)
.gitignore
README.md
```

**Rule of thumb:**  
> One folder per person. One owner per file.  
> Do not modify or commit files in someone else's folder unless explicitly agreed.

---

## Git workflow (VERY IMPORTANT)

### 1. Before starting to work

Always sync with the remote `main`:

```bash
git checkout main
git pull --rebase origin main
```

You can make this the default behaviour:

```bash
git config pull.rebase true           # or: git config --global pull.rebase true
```

---

### 2. After doing some work in *your* folder

Example for Alessandro (`PalumboBoss/`).  
Others just replace the folder name (`BiagiBoss/`, `CortoBoss/`, etc.):

```bash
git status
git add PalumboBoss/
git commit -m "Description of the work"
git pull --rebase origin main
git push origin main
```

**Key rule:**  
> Never use `git add .` from the repo root.  
> Always stage only your own folder.

---

## Working with other people's code

### Running someone else’s notebook

You may freely run code from other folders:

```bash
cd BiagiBoss/
jupyter notebook file.ipynb
```

Running a notebook is fine **as long as you do NOT commit or push it**.

If running the notebook causes the file to appear as modified, DO NOT commit it.

If needed, undo accidentally staged changes:

```bash
git restore --staged BiagiBoss/file.ipynb
git restore BiagiBoss/file.ipynb
```

---

### If you want to modify someone else’s code

Two proper options:

#### Option 1 — Copy the file into your own folder

```bash
cp BiagiBoss/file.ipynb PalumboBoss/biagi_trial.ipynb
```

#### Option 2 — Create a branch and propose changes

```bash
git checkout -b feature-biagi-suggestion
# edit in BiagiBoss/
git commit -am "Suggestion"
git push origin feature-biagi-suggestion
```

Then open a Pull Request.

**Never push modifications to someone else's files on `main` without agreement.**

---

## Jupyter Notebook Best Practices

Notebooks (`*.ipynb`) often create conflicts because they store outputs and metadata.

To minimise issues:

### 1. One owner per notebook
Only the owner commits changes to their notebook.

### 2. Avoid committing outputs when possible
Before committing, optionally:

- `Kernel → Restart & Clear Output`

This keeps diffs smaller.

### 3. Never push notebooks that are not yours
Running them locally is fine.  
Pushing them is not.

### 4. If a conflict happens
To keep your local version:

```bash
git checkout --ours PalumboBoss/file.ipynb
git add PalumboBoss/file.ipynb
git rebase --continue
```

To keep the remote version:

```bash
git checkout --theirs PalumboBoss/file.ipynb
git add PalumboBoss/file.ipynb
git rebase --continue
```

---

## Quick checklist before every push

1. `git status`
2. Are all modified files **inside your folder**?
   - YES → proceed  
   - NO → clean up:
     ```bash
     git restore --staged .
     git restore .
     ```
     Then stage again your folder only:
     ```
     git add PalumboBoss/
     ```
3. `git pull --rebase origin main`
4. `git push origin main`

---

## Italian Quick Summary

- Ognuno lavora solo nella propria cartella.  
- Si fa sempre `git pull --rebase origin main` prima di lavorare e prima del push.  
- Si usa sempre `git add <cartella_personale>/`.  
- Si possono eseguire i notebook degli altri, ma non committarli.  
- Se vuoi modificare i file di un altro, copiali nella tua cartella o crea un branch dedicato.

---
