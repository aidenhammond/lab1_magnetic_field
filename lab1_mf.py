from vpython import *
scene.height = 760 
scene.width = 1024

mzofp = 1e-7 # permeability over 4*pi
I = 3 
l = 0 
lenght = 0.4 
N = 40 # N dl's around the loop 
dl = lenght / N 
wire_list = [vector(0, 0.05, 0.05)] 
i = 0 
thetamax = 2 * pi 
R = 1 
theta = 0 
dtheta = pi / 6 
obs = [] 
obs_arrow = [] 
j = 0

while theta < thetamax:
  obs.append(vector(cos(theta), sin(theta), 0))
  obs_arrow += [arrow(pos=obs[j], axis=vector(0, 0, 0))] 
  theta += dtheta 
  j += 1

while l <= lenght - 0.02: 
  if l < 0.09: 
    wire_list.append(wire_list[i] + vector(0, -dl, 0)) 
    i += 1 
  elif 0.09 <= l < 0.19: 
    wire_list.append(wire_list[i] + vector(0, 0, -dl)) 
    i += 1 
  elif 0.19 <= l < 0.28: 
    wire_list.append(wire_list[i] + vector(0, dl, 0)) 
    i += 1 
  elif 0.28 <= l < 0.38: 
    wire_list.append(wire_list[i] + vector(0, 0, dl)) 
    i += 1 
  l += dl

wire = curve(pos=wire_list, color=color.orange)
iobs = 0 
while iobs < len(obs_arrow): 
  B = vector(0, 0, 0) 
  i = 0 
  while i < N - (N/20): 
    rate(1000) 
    dl = wire.point(i + 1)["pos"] - wire.point(i)["pos"] 
    loc = wire.point(i)["pos"] + dl/2 
    r = obs_arrow[iobs].pos - loc 
    rhat = r/mag(r) 
    B += mzofp * I * cross(dl, rhat) / mag(r) ** 2 
    i += 1 
  obs_arrow[iobs].axis = B*1e8 
  iobs += 1

print(obs_arrow[0].axis)


while True:
  continue
