from Translator import Translator

translator = Translator()
translator.read_in_data()
translator.process_node_information()
translator.process_edge_information()
translator.process_group_information()
translator.process_output_data()
translator.write_output_data()
