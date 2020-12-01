import PIL
from PIL import Image, ImageDraw


def draw(A, H):
    img = Image.new('RGB', (540, 960), color='white')
    pixels = img.load()

    for coord in A:
        pixels[coord[0], coord[1]] = (0, 0, 0)

    draw = ImageDraw.Draw(img)

    for i in range(0, len(H)-1):
        draw.line((A[H[i]][0], A[H[i]][1], A[H[i+1]][0], A[H[i+1]][1]), fill="blue", width=1)

    img.save('result.png')

def open_file():
    A = []
    file = open("DS1.txt", "r")
    for line in file:
        coord = line.split()
        coord[0] = int(coord[0])
        coord[1] = int(coord[1])
        A.append([coord[0], coord[1]])
    file.close()
    return A

def rotate(A, B, C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])


def jarvis(A):
  n = len(A)
  P = [i for i in range(0, n)]
  for i in range(0, n):
    if A[P[i]][0] < A[P[0]][0]:
      P[i], P[0] = P[0], P[i]
  H = [P[0]]
  del P[0]
  P.append(H[0])
  while True:
    right = 0
    for i in range(1,len(P)):
      if rotate(A[H[-1]],A[P[right]],A[P[i]])<0:
        right = i
    if P[right]==H[0]:
      break
    else:
      H.append(P[right])
      del P[right]
  return H

A = open_file()
H = jarvis(A)
draw(A, H)