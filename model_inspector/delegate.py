# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_delegate.ipynb (unless otherwise specified).

__all__ = ['delegates']

# Cell
import inspect
import textwrap

# Cell
def delegates(to=None, keep=False):
    """Decorator: replace `**kwargs` in signature with params from `to`

    Adapted from https://fastcore.fast.ai/meta.html#delegates
    """

    def _f(f):
        if to is None:
            to_f, from_f = f.__base__.__init__, f.__init__
        else:
            to_f, from_f = to, f
        sig = inspect.signature(from_f)
        sigd = dict(sig.parameters)
        k = sigd.pop("kwargs")
        s2 = {
            k: v
            for k, v in inspect.signature(to_f).parameters.items()
            if v.default != inspect.Parameter.empty and k not in sigd
        }
        sigd.update(s2)
        if keep:
            sigd["kwargs"] = k
        from_f.__signature__ = sig.replace(parameters=sigd.values())
        f.__doc__ += f"""
        
        Remaining parameters are passed to `{to.__module__}.{to.__name__}`.
        """
        return f

    return _f