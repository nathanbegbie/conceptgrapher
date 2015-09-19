from Nodes import FactNode, ConceptNode, MisconNode, ScaseNode
from Translator import Translator


class TestTranslator:
    def test_node_creation(self):
        translator = Translator("test1.map", "test2.map")
        translator.read_in_data()
        translator.process_node_information()
        # test1.map
        # Test that nodes are there
        assert "TEST101" in translator.graph.nodeDict
        assert "TEST102" in translator.graph.nodeDict
        assert "TEST103" in translator.graph.nodeDict
        assert "TEST104" in translator.graph.nodeDict
        assert "TEST201" in translator.graph.nodeDict
        assert "TEST202" in translator.graph.nodeDict
        assert "TEST203" in translator.graph.nodeDict
        assert "TEST204" in translator.graph.nodeDict
        assert "TEST205" in translator.graph.nodeDict
        assert "TEST301" in translator.graph.nodeDict
        assert "TEST302" in translator.graph.nodeDict
        assert "TEST401" in translator.graph.nodeDict
        assert "TEST402" in translator.graph.nodeDict
        # test that the type of node is correct
        assert isinstance(translator.graph.nodeDict["TEST101"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["TEST102"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["TEST103"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["TEST104"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["TEST201"], FactNode)
        assert isinstance(translator.graph.nodeDict["TEST202"], FactNode)
        assert isinstance(translator.graph.nodeDict["TEST203"], FactNode)
        assert isinstance(translator.graph.nodeDict["TEST204"], FactNode)
        assert isinstance(translator.graph.nodeDict["TEST205"], FactNode)
        assert isinstance(translator.graph.nodeDict["TEST301"], MisconNode)
        assert isinstance(translator.graph.nodeDict["TEST302"], MisconNode)
        assert isinstance(translator.graph.nodeDict["TEST401"], ScaseNode)
        assert isinstance(translator.graph.nodeDict["TEST402"], ScaseNode)
        # test that ID is correct
        assert translator.graph.nodeDict["TEST101"].ID == "TEST101"
        assert translator.graph.nodeDict["TEST102"].ID == "TEST102"
        assert translator.graph.nodeDict["TEST103"].ID == "TEST103"
        assert translator.graph.nodeDict["TEST104"].ID == "TEST104"
        assert translator.graph.nodeDict["TEST201"].ID == "TEST201"
        assert translator.graph.nodeDict["TEST202"].ID == "TEST202"
        assert translator.graph.nodeDict["TEST203"].ID == "TEST203"
        assert translator.graph.nodeDict["TEST204"].ID == "TEST204"
        assert translator.graph.nodeDict["TEST205"].ID == "TEST205"
        assert translator.graph.nodeDict["TEST301"].ID == "TEST301"
        assert translator.graph.nodeDict["TEST302"].ID == "TEST302"
        assert translator.graph.nodeDict["TEST401"].ID == "TEST401"
        assert translator.graph.nodeDict["TEST402"].ID == "TEST402"
        # test that content is copied across correctly
        assert translator.graph.nodeDict["TEST101"].content == (
            "The first concept from TESTMAP")
        assert translator.graph.nodeDict["TEST102"].content == (
            "The second concept from TESTMAP")
        assert translator.graph.nodeDict["TEST103"].content == (
            "The third concept from TESTMAP")
        assert translator.graph.nodeDict["TEST104"].content == (
            "The fourth concept from TESTMAP")
        assert translator.graph.nodeDict["TEST201"].content == (
            "The first fact from TESTMAP")
        assert translator.graph.nodeDict["TEST202"].content == (
            "The second fact from TESTMAP")
        assert translator.graph.nodeDict["TEST203"].content == (
            "The third fact from TESTMAP")
        assert translator.graph.nodeDict["TEST204"].content == (
            "The fourth fact from TESTMAP")
        assert translator.graph.nodeDict["TEST205"].content == (
            "The fifth fact from TESTMAP")
        assert translator.graph.nodeDict["TEST301"].content == (
            "The first miscon from TESTMAP")
        assert translator.graph.nodeDict["TEST302"].content == (
            "The second miscon from TESTMAP")
        assert translator.graph.nodeDict["TEST401"].content == (
            "The first scase from TESTMAP")
        assert translator.graph.nodeDict["TEST402"].content == (
            "The second scase from TESTMAP")

        # test2.map

        assert "REST101" in translator.graph.nodeDict
        assert "REST102" in translator.graph.nodeDict
        assert "REST103" in translator.graph.nodeDict
        assert "REST104" in translator.graph.nodeDict
        assert "REST201" in translator.graph.nodeDict
        assert "REST202" in translator.graph.nodeDict
        assert "REST203" in translator.graph.nodeDict
        assert "REST204" in translator.graph.nodeDict
        assert "REST205" in translator.graph.nodeDict
        assert "REST301" in translator.graph.nodeDict
        assert "REST302" in translator.graph.nodeDict
        assert "REST401" in translator.graph.nodeDict
        assert "REST402" in translator.graph.nodeDict

        assert isinstance(translator.graph.nodeDict["REST101"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["REST102"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["REST103"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["REST104"], ConceptNode)
        assert isinstance(translator.graph.nodeDict["REST201"], FactNode)
        assert isinstance(translator.graph.nodeDict["REST202"], FactNode)
        assert isinstance(translator.graph.nodeDict["REST203"], FactNode)
        assert isinstance(translator.graph.nodeDict["REST204"], FactNode)
        assert isinstance(translator.graph.nodeDict["REST205"], FactNode)
        assert isinstance(translator.graph.nodeDict["REST301"], MisconNode)
        assert isinstance(translator.graph.nodeDict["REST302"], MisconNode)
        assert isinstance(translator.graph.nodeDict["REST401"], ScaseNode)
        assert isinstance(translator.graph.nodeDict["REST402"], ScaseNode)

        assert translator.graph.nodeDict["REST101"].ID == "REST101"
        assert translator.graph.nodeDict["REST102"].ID == "REST102"
        assert translator.graph.nodeDict["REST103"].ID == "REST103"
        assert translator.graph.nodeDict["REST104"].ID == "REST104"
        assert translator.graph.nodeDict["REST201"].ID == "REST201"
        assert translator.graph.nodeDict["REST202"].ID == "REST202"
        assert translator.graph.nodeDict["REST203"].ID == "REST203"
        assert translator.graph.nodeDict["REST204"].ID == "REST204"
        assert translator.graph.nodeDict["REST205"].ID == "REST205"
        assert translator.graph.nodeDict["REST301"].ID == "REST301"
        assert translator.graph.nodeDict["REST302"].ID == "REST302"
        assert translator.graph.nodeDict["REST401"].ID == "REST401"
        assert translator.graph.nodeDict["REST402"].ID == "REST402"

        assert translator.graph.nodeDict["REST101"].content == (
            "The first concept from RESTMAP")
        assert translator.graph.nodeDict["REST102"].content == (
            "The second concept from RESTMAP")
        assert translator.graph.nodeDict["REST103"].content == (
            "The third concept from RESTMAP")
        assert translator.graph.nodeDict["REST104"].content == (
            "The fourth concept from RESTMAP")
        assert translator.graph.nodeDict["REST201"].content == (
            "The first fact from RESTMAP")
        assert translator.graph.nodeDict["REST202"].content == (
            "The second fact from RESTMAP")
        assert translator.graph.nodeDict["REST203"].content == (
            "The third fact from RESTMAP")
        assert translator.graph.nodeDict["REST204"].content == (
            "The fourth fact from RESTMAP")
        assert translator.graph.nodeDict["REST205"].content == (
            "The fifth fact from RESTMAP")
        assert translator.graph.nodeDict["REST301"].content == (
            "The first miscon from RESTMAP")
        assert translator.graph.nodeDict["REST302"].content == (
            "The second miscon from RESTMAP")
        assert translator.graph.nodeDict["REST401"].content == (
            "The first scase from RESTMAP")
        assert translator.graph.nodeDict["REST402"].content == (
            "The second scase from RESTMAP")

    def test_edge_creation(self):
        translator = Translator("test1.map", "test2.map")
        translator.read_in_data()
        translator.process_node_information()
        translator.process_edge_information()
        # test1.map
        assert "TEST101" in translator.graph.edgeDict
        assert "TEST201" in translator.graph.edgeDict
        assert "TEST102" in translator.graph.edgeDict
        assert "TEST103" in translator.graph.edgeDict
        assert "TEST104" in translator.graph.edgeDict

        assert translator.graph.edgeDict["TEST101"].source == "TEST101"
        assert translator.graph.edgeDict["TEST201"].source == "TEST201"
        assert translator.graph.edgeDict["TEST102"].source == "TEST102"
        assert translator.graph.edgeDict["TEST103"].source == "TEST103"
        assert translator.graph.edgeDict["TEST104"].source == "TEST104"

        assert "TEST201" in translator.graph.edgeDict["TEST101"].targets
        assert "TEST301" in translator.graph.edgeDict["TEST101"].targets
        assert "TEST401" in translator.graph.edgeDict["TEST101"].targets
        assert len(translator.graph.edgeDict["TEST101"].targets) == 3

        assert "TEST202" in translator.graph.edgeDict["TEST201"].targets
        assert len(translator.graph.edgeDict["TEST201"].targets) == 1

        assert "TEST103" in translator.graph.edgeDict["TEST102"].targets
        assert len(translator.graph.edgeDict["TEST102"].targets) == 1

        assert "TEST104" in translator.graph.edgeDict["TEST103"].targets
        assert "TEST205" in translator.graph.edgeDict["TEST103"].targets
        assert "TEST302" in translator.graph.edgeDict["TEST103"].targets
        assert "TEST402" in translator.graph.edgeDict["TEST103"].targets
        assert len(translator.graph.edgeDict["TEST103"].targets) == 4

        assert "TEST203" in translator.graph.edgeDict["TEST104"].targets
        assert "TEST204" in translator.graph.edgeDict["TEST104"].targets
        assert len(translator.graph.edgeDict["TEST104"].targets) == 2

        # test2.map
        assert "REST101" in translator.graph.edgeDict
        assert "REST201" in translator.graph.edgeDict
        assert "REST102" in translator.graph.edgeDict
        assert "REST103" in translator.graph.edgeDict
        assert "REST104" in translator.graph.edgeDict

        assert translator.graph.edgeDict["REST101"].source == "REST101"
        assert translator.graph.edgeDict["REST201"].source == "REST201"
        assert translator.graph.edgeDict["REST102"].source == "REST102"
        assert translator.graph.edgeDict["REST103"].source == "REST103"
        assert translator.graph.edgeDict["REST104"].source == "REST104"

        assert "REST201" in translator.graph.edgeDict["REST101"].targets
        assert "REST301" in translator.graph.edgeDict["REST101"].targets
        assert "REST401" in translator.graph.edgeDict["REST101"].targets
        assert len(translator.graph.edgeDict["REST101"].targets) == 3

        assert "REST202" in translator.graph.edgeDict["REST201"].targets
        assert len(translator.graph.edgeDict["REST201"].targets) == 1

        assert "REST103" in translator.graph.edgeDict["REST102"].targets
        assert len(translator.graph.edgeDict["REST102"].targets) == 1

        assert "REST104" in translator.graph.edgeDict["REST103"].targets
        assert "REST205" in translator.graph.edgeDict["REST103"].targets
        assert "REST302" in translator.graph.edgeDict["REST103"].targets
        assert "REST402" in translator.graph.edgeDict["REST103"].targets
        assert len(translator.graph.edgeDict["REST103"].targets) == 4

        assert "REST203" in translator.graph.edgeDict["REST104"].targets
        assert "REST204" in translator.graph.edgeDict["REST104"].targets
        assert len(translator.graph.edgeDict["REST104"].targets) == 2

        # for the outer dependency declared at the end of test2.map
        assert "TEST204" in translator.graph.edgeDict
        assert translator.graph.edgeDict["TEST204"].source == "TEST204"
        assert "REST101" in translator.graph.edgeDict["TEST204"].targets
        assert len(translator.graph.edgeDict["TEST204"].targets) == 1

        assert len(translator.graph.edgeDict) == 11

    def test_group_creation(self):
        translator = Translator("test1.map", "test2.map")
        translator.read_in_data()
        translator.process_node_information()
        translator.process_edge_information()
        translator.process_group_information()
        assert "TEST000" in translator.graph.groupDict
        assert "TEST001" in translator.graph.groupDict
        assert "TEST002" in translator.graph.groupDict
        assert "REST000" in translator.graph.groupDict
        assert "REST001" in translator.graph.groupDict
        assert "REST002" in translator.graph.groupDict

        assert len(translator.graph.groupDict) == 6

        assert translator.graph.groupDict["TEST000"].content == (
            "The first group from TESTMAP")
        assert translator.graph.groupDict["TEST001"].content == (
            "The second group from TESTMAP")
        assert translator.graph.groupDict["TEST002"].content == (
            "The third group from TESTMAP")
        assert translator.graph.groupDict["REST000"].content == (
            "The first group from RESTMAP")
        assert translator.graph.groupDict["REST001"].content == (
            "The second group from RESTMAP")
        assert translator.graph.groupDict["REST002"].content == (
            "The third group from RESTMAP")

        assert "TEST101" in translator.groups["TEST000"]
        assert "TEST102" in translator.groups["TEST000"]
        assert "TEST103" in translator.groups["TEST000"]
        assert "TEST104" in translator.groups["TEST000"]
        assert "TEST201" in translator.groups["TEST000"]
        assert "TEST202" in translator.groups["TEST000"]
        assert "TEST203" in translator.groups["TEST000"]
        assert "TEST204" in translator.groups["TEST000"]
        assert "TEST205" in translator.groups["TEST000"]
        assert "TEST301" in translator.groups["TEST000"]
        assert "TEST302" in translator.groups["TEST000"]
        assert "TEST401" in translator.groups["TEST000"]
        assert "TEST402" in translator.groups["TEST000"]
        # make sure groups are not included
        assert "TEST001" not in translator.groups["TEST000"]
        assert "TEST002" not in translator.groups["TEST000"]

        assert len(translator.groups["TEST000"]) == 13

        assert "TEST103" in translator.groups["TEST001"]
        assert "TEST104" in translator.groups["TEST001"]
        assert "TEST205" in translator.groups["TEST001"]
        assert "TEST302" in translator.groups["TEST001"]
        assert "TEST402" in translator.groups["TEST001"]
        assert "TEST203" in translator.groups["TEST001"]
        assert "TEST204" in translator.groups["TEST001"]

        assert "TEST002" not in translator.groups["TEST001"]

        assert len(translator.groups["TEST001"]) == 7

        assert "TEST104" in translator.groups["TEST002"]
        assert "TEST203" in translator.groups["TEST002"]
        assert "TEST204" in translator.groups["TEST002"]

        assert len(translator.groups["TEST002"]) == 3

        assert "REST101" in translator.groups["REST000"]
        assert "REST102" in translator.groups["REST000"]
        assert "REST103" in translator.groups["REST000"]
        assert "REST104" in translator.groups["REST000"]
        assert "REST201" in translator.groups["REST000"]
        assert "REST202" in translator.groups["REST000"]
        assert "REST203" in translator.groups["REST000"]
        assert "REST204" in translator.groups["REST000"]
        assert "REST205" in translator.groups["REST000"]
        assert "REST301" in translator.groups["REST000"]
        assert "REST302" in translator.groups["REST000"]
        assert "REST401" in translator.groups["REST000"]
        assert "REST402" in translator.groups["REST000"]
        # make sure groups are not included
        assert "REST001" not in translator.groups["REST000"]
        assert "REST002" not in translator.groups["REST000"]

        assert len(translator.groups["REST000"]) == 13

        assert "REST103" in translator.groups["REST001"]
        assert "REST104" in translator.groups["REST001"]
        assert "REST205" in translator.groups["REST001"]
        assert "REST302" in translator.groups["REST001"]
        assert "REST402" in translator.groups["REST001"]
        assert "REST203" in translator.groups["REST001"]
        assert "REST204" in translator.groups["REST001"]

        assert "REST002" not in translator.groups["REST001"]

        assert len(translator.groups["REST001"]) == 7

        assert "REST104" in translator.groups["REST002"]
        assert "REST203" in translator.groups["REST002"]
        assert "REST204" in translator.groups["REST002"]

        assert len(translator.groups["REST002"]) == 3
