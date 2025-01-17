class GithubActionLoginException(Exception):
    """
    在github action环境下登录异常
    """
    pass


class SameAccountTryLoginAtMultipleThreadsException(Exception):
    """
    单个账号尝试在多个线程/进程中同时登录

    一般出现于在超快速模式下skey中途过期，导致后续运行时同一个账号在同时运行多个活动时，同时检测到skey过期而同时登录的问题
    """
    pass


class DnfHelperChronicleTokenExpiredOrWrongException(Exception):
    """
    dnf助手编年史的token过期或者不对
    """
    pass
