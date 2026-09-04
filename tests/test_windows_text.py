from swebench.harness.run_evaluation import _write_utf8_lf


def test_evaluator_text_artifacts_are_utf8_and_lf_only(tmp_path):
    path = tmp_path / "eval.sh"

    _write_utf8_lf(path, "#!/bin/bash\necho café\n")

    assert path.read_bytes() == b"#!/bin/bash\necho caf\xc3\xa9\n"
