# Gera os ícones do app a partir da roda de emoções (fatias coloridas das 10 famílias)
from PIL import Image, ImageDraw

CORES = ['#C9922E','#3F7A6B','#C15B6E','#A9862E','#8C7B9B',
         '#3F5578','#5F6B41','#9C5B3C','#A8402F','#6B6459']
FUNDO = '#FBF3EC'
MIOLO = '#8C2F39'

def desenhar(tamanho, margem_rel):
    # Supersampling 4x para bordas suaves
    S = tamanho * 4
    img = Image.new('RGBA', (S, S), FUNDO)
    d = ImageDraw.Draw(img)
    m = int(S * margem_rel)
    caixa = [m, m, S - m, S - m]
    passo = 360 / len(CORES)
    for i, cor in enumerate(CORES):
        d.pieslice(caixa, start=i*passo - 90, end=(i+1)*passo - 90, fill=cor)
    # Miolo vinho, deixando o desenho legível em tamanho pequeno
    r = (caixa[2] - caixa[0]) * 0.30
    cx, cy = S/2, S/2
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=MIOLO)
    return img.resize((tamanho, tamanho), Image.LANCZOS)

# Ícones padrão (roda ocupando quase todo o quadro)
for t in (192, 512):
    desenhar(t, 0.08).convert('RGB').save(f'icons/icone-{t}.png')

# Ícone "maskable": o Android recorta as bordas, então a arte fica na zona segura central
desenhar(512, 0.20).convert('RGB').save('icons/icone-maskable-512.png')

print('ok')
