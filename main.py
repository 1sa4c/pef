from Truss import Truss
from Joint import Joint
from Load import Load
from Support import Support
from SupportType import SupportType
import numpy as np

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

