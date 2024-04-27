from torch import nn
import torch
import math
import torch.nn.functional as F
from clip import clip


class BEIPLUG(nn.Module):
    def __init__(self, config: None, tokenizer: None) -> None:
        super().__init__()
    
        visual_encoder = 2





if __name__ == "__main__":
    config = {"clip_name": "RN50"}
    clip_model, transform = initialize_clip(config)