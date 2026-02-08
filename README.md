# Machine Learning Lite Project Template

This project uses **MLflow** for experiment tracking, **Mamba** for environment management, and **Git** for code versioning.

Currently used as my Kaggle workflow.


## Setup Guide

### 1. Environment Installation

Install [Mamba](https://github.com/mamba-org/mamba) first, then run:

```bash
# Create the environment
mamba env create -f environment.yml

# Activate the environment
mamba activate MLproject

# [Optional] Clean up :D
mamba clean --all

```