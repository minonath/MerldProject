from ._GL_10 import *
from ._GL_11 import *
from ._GL_12 import *
from ._GL_13 import *
from ._GL_14 import *
from ._GL_15 import *
from ._GL_20 import *
from ._GL_21 import *
from ._GL_30 import *
from ._GL_31 import *
from ._GL_32 import *
from ._GL_33 import *
from ._GL_40 import *
from ._GL_41 import *
from ._GL_42 import *
from ._GL_43 import *
from ._GL_44 import *
from ._GL_45 import *
from ._GL_46 import *
from ._GL_ARB import *
from ._GL_KHR import *
from ._GL_AMD import *
from ._GL_APPLE import *
from ._GL_EXT import *
from ._GL_INTEL import *
from ._GL_MESA import *
from ._GL_NV import *
from ._GL_OVR import *


class OpenGLError(Exception):
    ...


def gl_get(name):
    return globals().get(name)
