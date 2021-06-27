import contextlib
import sys
import shutil

from pyke import knowledge_engine
from pyke import krb_traceback


dir_path = 'kb/compiled_krb/'

try:
    shutil.rmtree(dir_path)
except OSError as e:
    print("Error: %s : %s" % (dir_path, e.strerror))

engine = knowledge_engine.engine(__file__)


def bc_test_questions():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_simple_rules_questions')

    print("doing proof")
    cont = 0
    try:
        with engine.prove_goal('bc_simple_rules_questions.what_disease($malattia)') as gen:
            for vars, plan in gen:
                print("Malattia: %s" % (vars['malattia']))
                cont = cont + 1

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    if cont == 0:
        print("Malattia: nessuna o sconosciuta")

    print("done")
