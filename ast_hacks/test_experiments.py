from ast import parse, Module, FunctionDef
import inspect


def double_any[T](x: T) -> T:
    return x * 2


def test_double_any():
    tree = parse(inspect.getsource(double_any))
    match tree:
        case Module(body=[FunctionDef(type_params=tps)]):
            tv=tps[0]

    assert tv.name == 'T'
