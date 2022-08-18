# -*- coding: utf-8 -*-

############################################################################
#  This file is part of the 4D Light Field Benchmark.                      #
#                                                                          #
#  This work is licensed under the Creative Commons                        #
#  Attribution-NonCommercial-ShareAlike 4.0 International License.         #
#  To view a copy of this license,                                         #
#  visit http://creativecommons.org/licenses/by-nc-sa/4.0/.                #
#                                                                          #
#  Authors: Katrin Honauer & Ole Johannsen                                 #
#  Contact: contact@lightfield-analysis.net                                #
#  Website: www.lightfield-analysis.net                                    #
#                                                                          #
#  The 4D Light Field Benchmark was jointly created by the University of   #
#  Konstanz and the HCI at Heidelberg University. If you use any part of   #
#  the benchmark, please cite our paper "A dataset and evaluation          #
#  methodology for depth estimation on 4D light fields". Thanks!           #
#                                                                          #
#  @inproceedings{honauer2016benchmark,                                    #
#    title={A dataset and evaluation methodology for depth estimation on   #
#           4D light fields},                                              #
#    author={Honauer, Katrin and Johannsen, Ole and Kondermann, Daniel     #
#            and Goldluecke, Bastian},                                     #
#    booktitle={Asian Conference on Computer Vision},                      #
#    year={2016},                                                          #
#    organization={Springer}                                               #
#    }                                                                     #
#                                                                          #
############################################################################


from toolkit.utils.option_parser import OptionParser, ConverterOps


def main():
    parser = OptionParser([ConverterOps(input_help="path to depth map",
                                        output_help="path to disparity map")])

    depth_map_path, config_path, disp_map_path = parser.parse_args()

    from toolkit.scenes import PhotorealisticScene
    from toolkit.utils import file_io

    scene = PhotorealisticScene("demo", path_to_config=config_path)
    depth_map = file_io.read_file(depth_map_path)
    disp_map = scene.depth2disp(depth_map)
    file_io.write_file(disp_map, disp_map_path)


if __name__ == "__main__":
    main()
