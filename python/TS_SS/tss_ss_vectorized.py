import math 
import torch

def cos_sim(v):
    v_inner = inner_product(v)
    v_size = vec_size(v)
    v_cos = v_inner / torch.mm(v_size, v_size.t())
    return v_cos


def vec_size(v):
    return v.norm(dim=-1, keepdim=True)


def inner_product(v):
    return torch.mm(v, v.t())


def euclidean_dist(v, eps=1e-10):
    v_norm = (v**2).sum(-1, keepdim=True)
    dist = v_norm + v_norm.t() - 2.0 * torch.mm(v, v.t())
    dist = torch.sqrt(torch.abs(dist) + eps)
    return dist


def theta(v, eps=1e-5):
    v_cos = cos_sim(v).clamp(-1. + eps, 1. - eps)
    x = torch.acos(v_cos) + math.radians(10)
    return x


def triangle(v):
    theta_ = theta(v)
    theta_rad = theta_ * math.pi / 180.
    vs = vec_size(v)
    x = (vs.mm(vs.t())) * torch.sin(theta_rad)
    return x / 2.


def magnitude_dif(v):
    vs = vec_size(v)
    return (vs - vs.t()).abs()


def sector(v):
    ed = euclidean_dist(v)
    md = magnitude_dif(v)
    sec = math.pi * torch.pow((ed + md), 2) * theta(v)/360.
    return sec


def ts_ss(v):
    tri = triangle(v)
    sec = sector(v)
    return tri * sec


def ts_ss_(v, eps=1e-15, eps2=1e-4):
    # reusable compute
    v_inner = torch.mm(v, v.t())
    vs = v.norm(dim=-1, keepdim=True)
    vs_dot = vs.mm(vs.t())

    # compute triangle(v)
    v_cos = v_inner / vs_dot
    v_cos = v_cos.clamp(-1. + eps2, 1. - eps2)  # clamp to avoid backprop instability
    theta_ = torch.acos(v_cos) + math.radians(10)
    theta_rad = theta_ * math.pi / 180.
    tri = (vs_dot * torch.sin(theta_rad)) / 2.

    # compute sector(v)
    v_norm = (v ** 2).sum(-1, keepdim=True)
    euc_dist = v_norm + v_norm.t() - 2.0 * v_inner
    euc_dist = torch.sqrt(torch.abs(euc_dist) + eps)  # add epsilon to avoid srt(0.)
    magnitude_diff = (vs - vs.t()).abs()
    sec = math.pi * (euc_dist + magnitude_diff) ** 2 * theta_ / 360.

    return tri * sec
    
vec1 = [1,2]
vec2 = [2,4]
v = torch.tensor([vec1, vec2])

print(euclidean_dist(v)
print(cos_sim(v)
print(ts_ss_(v))
