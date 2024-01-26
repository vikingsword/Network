import torch
from torchtext.nn import MultiheadAttentionContainer, InProjContainer, ScaledDotProduct

embed_dim, num_heads, bsz = 10, 5, 64
in_proj_container = InProjContainer(torch.nn.Linear(embed_dim, embed_dim),
                                    torch.nn.Linear(embed_dim, embed_dim),
                                    torch.nn.Linear(embed_dim, embed_dim))
MHA = MultiheadAttentionContainer(num_heads,
                                  in_proj_container,
                                  ScaledDotProduct(),
                                  torch.nn.Linear(embed_dim, embed_dim))
query = torch.rand((21, bsz, embed_dim))
key = value = torch.rand((16, bsz, embed_dim))
attn_output, attn_weights = MHA(query, key, value)
print(attn_output.shape)
torch.Size([21, 64, 10])





