import torch.nn as nn


class PrisPeace(nn.Module):
    def __init__(
        self, 
        config,
        text_adapter,
        image_adapter,
        prismer_experts
    ):
        super(PrisPeace, self).__init__()
        # Config prismer expert object
        
