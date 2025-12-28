from my_project.core.logic import Processor


def test_processor_run():
    p = Processor("Test")
    assert p.run() == "Processing by Test"
