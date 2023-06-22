from Truss import Truss
from Joint import Joint
from Load import Load
from Support import Support
from SupportType import SupportType
import numpy as np

def boxprint(text: str, space=-1) -> None:
    total_space = space if space > 0 else (len(text) + 4)

    print('-' * total_space)
    print(f'|{text.center(total_space - 2)}|')
    print('-' * total_space)

print("""

    ██████╗ ███████╗███████╗    ██████╗ ██████╗  ██████╗  █████╗ 
    ██╔══██╗██╔════╝██╔════╝    ╚════██╗╚════██╗██╔═████╗██╔══██╗
    ██████╔╝█████╗  █████╗       █████╔╝ █████╔╝██║██╔██║╚█████╔╝
    ██╔═══╝ ██╔══╝  ██╔══╝       ╚═══██╗██╔═══╝ ████╔╝██║██╔══██╗
    ██║     ███████╗██║         ██████╔╝███████╗╚██████╔╝╚█████╔╝
    ╚═╝     ╚══════╝╚═╝         ╚═════╝ ╚══════╝ ╚═════╝  ╚════╝ 
                                                                 
      """
)

number_of_joints = int(input(' Digite o número de vertices: '))
number_of_bars = int(input(' Digite o número de barras: '))
number_of_supports = int(input(' Digite o número de suportes: '))
number_of_forces = int(input(' Digite o número de forças externas exercentes no conjunto: '))

print()


joints = list()
truss = Truss()

for i in range(number_of_joints):
    node_label = chr(ord('@') + i + 1)
    boxprint(f'Vertice {node_label}', 32)

    x1 = float(input(' X: '))
    y1 = float(input(' Y: '))

    joint = Joint(x1, y1)

    print()
    if number_of_supports != 0:
        input_case = str(input(' Suporte? (S/N) '))[0]
        if input_case in 'sS':
            print()
            print(' 1: Engaste')
            print(' 2: Deslizante')
            print(' 3: Pino')

            input_1 = int(input('\n '))

            if input_1 == 1:
                s1 = Support(SupportType.FIXED)
            elif input_1 == 2:
                s1 = Support(SupportType.ROLLER)
            else:
                s1 = Support(SupportType.PINNED)

            joint.set_support(s1)
            number_of_supports -= 1


    if number_of_forces != 0:
        input_case = str(input(' Forças externas? (S/N) '))[0]
        if input_case in 'sS':
            module = float(input(' Magnitude: '))
            angle = float(input(' Ângulo (°): '))

            force = Load(module, (angle * 2 * np.pi) / 360)

            number_of_forces -= 1

            joint.add_load(force)

    joints.append(joint)
    truss.add_joint(joint)
    print('-' * 32)
    print('\n')
    

print()
for j in range(number_of_bars):
    boxprint(f'Barra {j + 1}', 32)

    k = ord(str(input(' Do vértice: ')).upper()) - ord('@') - 1
    p = ord(str(input(' Ao vértice: ')).upper()) - ord('@') - 1
    truss.add_bar(joints[k], joints[p])

    print('-' * 32)
    print('\n')


truss.solve()
truss.show()

"""
joint_a = Joint(12, 9)
joint_b = Joint(36, 9)
joint_c = Joint(0, 0)
joint_d = Joint(24, 0)
joint_e = Joint(48, 0)

support_c = Support(SupportType.PINNED)
support_e = Support(SupportType.ROLLER)

joint_c.set_support(support_c)
joint_e.set_support(support_e)

load = Load(10, (-np.pi / 2))

joint_a.add_load(load)

truss = Truss()

truss.add_joint(joint_a)
truss.add_joint(joint_b)
truss.add_joint(joint_c)
truss.add_joint(joint_d)
truss.add_joint(joint_e)

truss.add_bar(joint_a, joint_b)
truss.add_bar(joint_a, joint_c)
truss.add_bar(joint_a, joint_d)
truss.add_bar(joint_c, joint_d)
truss.add_bar(joint_d, joint_e)
truss.add_bar(joint_b, joint_d)
truss.add_bar(joint_b, joint_e)

truss.solve()
truss.show()
"""

