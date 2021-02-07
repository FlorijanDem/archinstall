class RequirementError(BaseException):
	pass
class DiskError(BaseException):
	pass
class UnknownFilesystemFormat(BaseException):
	pass
class ProfileError(BaseException):
	pass
class SysCallError(BaseException):
	pass
class ProfileNotFound(BaseException):
	pass
class HardwareIncompatibilityError(BaseException):
	pass