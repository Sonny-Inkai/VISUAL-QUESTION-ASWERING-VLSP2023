from .image_experts.prismer import ImageExperts
#from .adapters.text import TextAdapter
from .transformer.transformer_encoder import TransformerEncoder
import torch.nn as nn

class ModelWrapper(nn.Moudle):
    def __init__(
        self, 
        config, 
        tokenizer,

    ):
        super(ModelWrapper, self).__init__()
        self.config = config
        embed_dim = config.embed_dim
        attention_heads = config.attention_heads

        #self.text_adapter = TextAdapter(config=config.text_adapter, embed_dim=embed_dim, attention_heads=attention_heads
        #                               , src_dict=src_dict, num_layers=num_layers)
        
        self.image_experts = ImageExperts(config=self.config.image_experts)
        # return ViT model
        self.image_encoder = self.image_experts.expert_encoder

        self.text_encoder = tokenizer(config=config.text_encoder)

    

    def forward(self, image, question, answer, ):
        image_encoder = self.image_encoder(self.config.image_experts['experts'])
        






