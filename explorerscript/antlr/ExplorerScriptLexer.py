# Generated from ExplorerScript.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,92,825,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,1,0,1,
        0,1,1,1,1,1,1,3,1,213,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,
        9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,
        18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,
        21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,
        23,1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,
        26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,
        28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,
        32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,
        34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,
        37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,
        39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,
        41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,
        45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,
        46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,
        48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,
        50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,
        52,1,52,1,53,1,53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,
        54,1,54,1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,
        55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,
        56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,
        56,1,56,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,
        57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,57,1,
        58,1,58,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,1,60,1,60,1,61,1,
        61,1,62,1,62,1,62,5,62,582,8,62,10,62,12,62,585,9,62,1,62,1,62,1,
        62,1,62,5,62,591,8,62,10,62,12,62,594,9,62,1,62,3,62,597,8,62,1,
        63,1,63,1,63,3,63,602,8,63,1,64,1,64,1,64,1,64,1,64,1,65,1,65,1,
        65,1,65,1,66,1,66,1,66,1,66,1,66,1,66,1,66,1,66,1,66,1,66,1,67,1,
        67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,68,1,68,1,68,1,
        68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,69,1,69,1,
        69,1,69,1,69,1,69,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,70,1,
        71,1,71,1,71,1,71,1,71,1,71,1,71,1,71,1,71,1,72,1,72,1,73,1,73,1,
        73,1,74,1,74,1,74,1,75,1,75,1,75,1,75,3,75,684,8,75,1,76,3,76,687,
        8,76,1,76,1,76,5,76,691,8,76,10,76,12,76,694,9,76,1,76,3,76,697,
        8,76,1,76,4,76,700,8,76,11,76,12,76,701,3,76,704,8,76,1,77,3,77,
        707,8,77,1,77,1,77,1,77,4,77,712,8,77,11,77,12,77,713,1,78,3,78,
        717,8,78,1,78,1,78,1,78,4,78,722,8,78,11,78,12,78,723,1,79,3,79,
        727,8,79,1,79,1,79,1,79,4,79,732,8,79,11,79,12,79,733,1,80,1,80,
        1,81,1,81,1,82,1,82,1,83,1,83,1,84,1,84,1,85,1,85,1,86,1,86,1,87,
        1,87,1,88,1,88,1,89,1,89,1,89,1,90,1,90,1,90,1,90,3,90,761,8,90,
        1,90,1,90,1,91,1,91,1,92,1,92,1,92,1,93,1,93,1,94,1,94,1,95,1,95,
        1,96,1,96,1,97,1,97,1,98,4,98,781,8,98,11,98,12,98,782,1,99,1,99,
        3,99,787,8,99,1,99,3,99,790,8,99,1,99,1,99,3,99,794,8,99,1,100,1,
        100,1,100,1,100,5,100,800,8,100,10,100,12,100,803,9,100,1,100,1,
        100,1,100,3,100,808,8,100,1,101,1,101,1,101,1,101,5,101,814,8,101,
        10,101,12,101,817,9,101,1,102,1,102,5,102,821,8,102,10,102,12,102,
        824,9,102,1,801,0,103,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,
        21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,
        32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,
        43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,
        107,54,109,55,111,56,113,57,115,58,117,59,119,60,121,61,123,62,125,
        63,127,64,129,65,131,66,133,67,135,68,137,69,139,70,141,71,143,72,
        145,73,147,74,149,75,151,76,153,77,155,78,157,79,159,80,161,81,163,
        82,165,83,167,84,169,85,171,86,173,87,175,88,177,89,179,90,181,91,
        183,92,185,0,187,0,189,0,191,0,193,0,195,0,197,0,199,0,201,0,203,
        0,205,0,1,0,16,4,0,10,10,12,13,39,39,92,92,4,0,10,10,12,13,34,34,
        92,92,1,0,36,36,1,0,126,126,2,0,79,79,111,111,2,0,88,88,120,120,
        2,0,66,66,98,98,1,0,49,57,1,0,48,57,1,0,48,55,3,0,48,57,65,70,97,
        102,1,0,48,49,3,0,9,10,13,13,32,32,2,0,10,10,13,13,3,0,65,90,95,
        95,97,122,4,0,48,57,65,90,95,95,97,122,847,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,
        0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,
        0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,
        0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,
        0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,
        0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,
        0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,
        0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,
        0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,
        0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,
        1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,
        0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,
        0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,
        141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,
        0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,157,1,0,0,0,0,159,
        1,0,0,0,0,161,1,0,0,0,0,163,1,0,0,0,0,165,1,0,0,0,0,167,1,0,0,0,
        0,169,1,0,0,0,0,171,1,0,0,0,0,173,1,0,0,0,0,175,1,0,0,0,0,177,1,
        0,0,0,0,179,1,0,0,0,0,181,1,0,0,0,0,183,1,0,0,0,1,207,1,0,0,0,3,
        212,1,0,0,0,5,214,1,0,0,0,7,220,1,0,0,0,9,225,1,0,0,0,11,227,1,0,
        0,0,13,229,1,0,0,0,15,231,1,0,0,0,17,234,1,0,0,0,19,237,1,0,0,0,
        21,240,1,0,0,0,23,243,1,0,0,0,25,245,1,0,0,0,27,247,1,0,0,0,29,251,
        1,0,0,0,31,254,1,0,0,0,33,257,1,0,0,0,35,260,1,0,0,0,37,263,1,0,
        0,0,39,266,1,0,0,0,41,270,1,0,0,0,43,275,1,0,0,0,45,280,1,0,0,0,
        47,287,1,0,0,0,49,293,1,0,0,0,51,296,1,0,0,0,53,303,1,0,0,0,55,308,
        1,0,0,0,57,316,1,0,0,0,59,321,1,0,0,0,61,328,1,0,0,0,63,335,1,0,
        0,0,65,339,1,0,0,0,67,344,1,0,0,0,69,353,1,0,0,0,71,359,1,0,0,0,
        73,370,1,0,0,0,75,376,1,0,0,0,77,383,1,0,0,0,79,393,1,0,0,0,81,399,
        1,0,0,0,83,405,1,0,0,0,85,410,1,0,0,0,87,420,1,0,0,0,89,427,1,0,
        0,0,91,434,1,0,0,0,93,447,1,0,0,0,95,453,1,0,0,0,97,458,1,0,0,0,
        99,463,1,0,0,0,101,471,1,0,0,0,103,477,1,0,0,0,105,483,1,0,0,0,107,
        488,1,0,0,0,109,492,1,0,0,0,111,507,1,0,0,0,113,521,1,0,0,0,115,
        540,1,0,0,0,117,564,1,0,0,0,119,570,1,0,0,0,121,574,1,0,0,0,123,
        576,1,0,0,0,125,596,1,0,0,0,127,601,1,0,0,0,129,603,1,0,0,0,131,
        608,1,0,0,0,133,612,1,0,0,0,135,622,1,0,0,0,137,633,1,0,0,0,139,
        647,1,0,0,0,141,653,1,0,0,0,143,662,1,0,0,0,145,671,1,0,0,0,147,
        673,1,0,0,0,149,676,1,0,0,0,151,683,1,0,0,0,153,703,1,0,0,0,155,
        706,1,0,0,0,157,716,1,0,0,0,159,726,1,0,0,0,161,735,1,0,0,0,163,
        737,1,0,0,0,165,739,1,0,0,0,167,741,1,0,0,0,169,743,1,0,0,0,171,
        745,1,0,0,0,173,747,1,0,0,0,175,749,1,0,0,0,177,751,1,0,0,0,179,
        753,1,0,0,0,181,760,1,0,0,0,183,764,1,0,0,0,185,766,1,0,0,0,187,
        769,1,0,0,0,189,771,1,0,0,0,191,773,1,0,0,0,193,775,1,0,0,0,195,
        777,1,0,0,0,197,780,1,0,0,0,199,784,1,0,0,0,201,795,1,0,0,0,203,
        809,1,0,0,0,205,818,1,0,0,0,207,208,5,59,0,0,208,2,1,0,0,0,209,213,
        3,73,36,0,210,213,3,75,37,0,211,213,3,77,38,0,212,209,1,0,0,0,212,
        210,1,0,0,0,212,211,1,0,0,0,213,4,1,0,0,0,214,215,5,70,0,0,215,216,
        5,65,0,0,216,217,5,76,0,0,217,218,5,83,0,0,218,219,5,69,0,0,219,
        6,1,0,0,0,220,221,5,84,0,0,221,222,5,82,0,0,222,223,5,85,0,0,223,
        224,5,69,0,0,224,8,1,0,0,0,225,226,5,61,0,0,226,10,1,0,0,0,227,228,
        5,60,0,0,228,12,1,0,0,0,229,230,5,62,0,0,230,14,1,0,0,0,231,232,
        5,61,0,0,232,233,5,61,0,0,233,16,1,0,0,0,234,235,5,60,0,0,235,236,
        5,61,0,0,236,18,1,0,0,0,237,238,5,62,0,0,238,239,5,61,0,0,239,20,
        1,0,0,0,240,241,5,33,0,0,241,242,5,61,0,0,242,22,1,0,0,0,243,244,
        5,38,0,0,244,24,1,0,0,0,245,246,5,94,0,0,246,26,1,0,0,0,247,248,
        5,38,0,0,248,249,5,60,0,0,249,250,5,60,0,0,250,28,1,0,0,0,251,252,
        5,45,0,0,252,253,5,61,0,0,253,30,1,0,0,0,254,255,5,43,0,0,255,256,
        5,61,0,0,256,32,1,0,0,0,257,258,5,42,0,0,258,259,5,61,0,0,259,34,
        1,0,0,0,260,261,5,47,0,0,261,262,5,61,0,0,262,36,1,0,0,0,263,264,
        5,124,0,0,264,265,5,124,0,0,265,38,1,0,0,0,266,267,5,110,0,0,267,
        268,5,111,0,0,268,269,5,116,0,0,269,40,1,0,0,0,270,271,5,106,0,0,
        271,272,5,117,0,0,272,273,5,109,0,0,273,274,5,112,0,0,274,42,1,0,
        0,0,275,276,5,99,0,0,276,277,5,97,0,0,277,278,5,108,0,0,278,279,
        5,108,0,0,279,44,1,0,0,0,280,281,5,105,0,0,281,282,5,109,0,0,282,
        283,5,112,0,0,283,284,5,111,0,0,284,285,5,114,0,0,285,286,5,116,
        0,0,286,46,1,0,0,0,287,288,5,109,0,0,288,289,5,97,0,0,289,290,5,
        99,0,0,290,291,5,114,0,0,291,292,5,111,0,0,292,48,1,0,0,0,293,294,
        5,105,0,0,294,295,5,102,0,0,295,50,1,0,0,0,296,297,5,101,0,0,297,
        298,5,108,0,0,298,299,5,115,0,0,299,300,5,101,0,0,300,301,5,105,
        0,0,301,302,5,102,0,0,302,52,1,0,0,0,303,304,5,101,0,0,304,305,5,
        108,0,0,305,306,5,115,0,0,306,307,5,101,0,0,307,54,1,0,0,0,308,309,
        5,102,0,0,309,310,5,111,0,0,310,311,5,114,0,0,311,312,5,101,0,0,
        312,313,5,118,0,0,313,314,5,101,0,0,314,315,5,114,0,0,315,56,1,0,
        0,0,316,317,5,119,0,0,317,318,5,105,0,0,318,319,5,116,0,0,319,320,
        5,104,0,0,320,58,1,0,0,0,321,322,5,115,0,0,322,323,5,119,0,0,323,
        324,5,105,0,0,324,325,5,116,0,0,325,326,5,99,0,0,326,327,5,104,0,
        0,327,60,1,0,0,0,328,329,5,114,0,0,329,330,5,101,0,0,330,331,5,116,
        0,0,331,332,5,117,0,0,332,333,5,114,0,0,333,334,5,110,0,0,334,62,
        1,0,0,0,335,336,5,101,0,0,336,337,5,110,0,0,337,338,5,100,0,0,338,
        64,1,0,0,0,339,340,5,104,0,0,340,341,5,111,0,0,341,342,5,108,0,0,
        342,343,5,100,0,0,343,66,1,0,0,0,344,345,5,99,0,0,345,346,5,111,
        0,0,346,347,5,110,0,0,347,348,5,116,0,0,348,349,5,105,0,0,349,350,
        5,110,0,0,350,351,5,117,0,0,351,352,5,101,0,0,352,68,1,0,0,0,353,
        354,5,98,0,0,354,355,5,114,0,0,355,356,5,101,0,0,356,357,5,97,0,
        0,357,358,5,107,0,0,358,70,1,0,0,0,359,360,5,98,0,0,360,361,5,114,
        0,0,361,362,5,101,0,0,362,363,5,97,0,0,363,364,5,107,0,0,364,365,
        5,95,0,0,365,366,5,108,0,0,366,367,5,111,0,0,367,368,5,111,0,0,368,
        369,5,112,0,0,369,72,1,0,0,0,370,371,5,97,0,0,371,372,5,99,0,0,372,
        373,5,116,0,0,373,374,5,111,0,0,374,375,5,114,0,0,375,74,1,0,0,0,
        376,377,5,111,0,0,377,378,5,98,0,0,378,379,5,106,0,0,379,380,5,101,
        0,0,380,381,5,99,0,0,381,382,5,116,0,0,382,76,1,0,0,0,383,384,5,
        112,0,0,384,385,5,101,0,0,385,386,5,114,0,0,386,387,5,102,0,0,387,
        388,5,111,0,0,388,389,5,114,0,0,389,390,5,109,0,0,390,391,5,101,
        0,0,391,392,5,114,0,0,392,78,1,0,0,0,393,394,5,118,0,0,394,395,5,
        97,0,0,395,396,5,108,0,0,396,397,5,117,0,0,397,398,5,101,0,0,398,
        80,1,0,0,0,399,400,5,100,0,0,400,401,5,101,0,0,401,402,5,98,0,0,
        402,403,5,117,0,0,403,404,5,103,0,0,404,82,1,0,0,0,405,406,5,101,
        0,0,406,407,5,100,0,0,407,408,5,105,0,0,408,409,5,116,0,0,409,84,
        1,0,0,0,410,411,5,118,0,0,411,412,5,97,0,0,412,413,5,114,0,0,413,
        414,5,105,0,0,414,415,5,97,0,0,415,416,5,116,0,0,416,417,5,105,0,
        0,417,418,5,111,0,0,418,419,5,110,0,0,419,86,1,0,0,0,420,421,5,114,
        0,0,421,422,5,97,0,0,422,423,5,110,0,0,423,424,5,100,0,0,424,425,
        5,111,0,0,425,426,5,109,0,0,426,88,1,0,0,0,427,428,5,115,0,0,428,
        429,5,101,0,0,429,430,5,99,0,0,430,431,5,116,0,0,431,432,5,111,0,
        0,432,433,5,114,0,0,433,90,1,0,0,0,434,435,5,100,0,0,435,436,5,117,
        0,0,436,437,5,110,0,0,437,438,5,103,0,0,438,439,5,101,0,0,439,440,
        5,111,0,0,440,441,5,110,0,0,441,442,5,95,0,0,442,443,5,109,0,0,443,
        444,5,111,0,0,444,445,5,100,0,0,445,446,5,101,0,0,446,92,1,0,0,0,
        447,448,5,109,0,0,448,449,5,101,0,0,449,450,5,110,0,0,450,451,5,
        117,0,0,451,452,5,50,0,0,452,94,1,0,0,0,453,454,5,109,0,0,454,455,
        5,101,0,0,455,456,5,110,0,0,456,457,5,117,0,0,457,96,1,0,0,0,458,
        459,5,99,0,0,459,460,5,97,0,0,460,461,5,115,0,0,461,462,5,101,0,
        0,462,98,1,0,0,0,463,464,5,100,0,0,464,465,5,101,0,0,465,466,5,102,
        0,0,466,467,5,97,0,0,467,468,5,117,0,0,468,469,5,108,0,0,469,470,
        5,116,0,0,470,100,1,0,0,0,471,472,5,99,0,0,472,473,5,108,0,0,473,
        474,5,101,0,0,474,475,5,97,0,0,475,476,5,114,0,0,476,102,1,0,0,0,
        477,478,5,114,0,0,478,479,5,101,0,0,479,480,5,115,0,0,480,481,5,
        101,0,0,481,482,5,116,0,0,482,104,1,0,0,0,483,484,5,105,0,0,484,
        485,5,110,0,0,485,486,5,105,0,0,486,487,5,116,0,0,487,106,1,0,0,
        0,488,489,5,115,0,0,489,490,5,99,0,0,490,491,5,110,0,0,491,108,1,
        0,0,0,492,493,5,100,0,0,493,494,5,117,0,0,494,495,5,110,0,0,495,
        496,5,103,0,0,496,497,5,101,0,0,497,498,5,111,0,0,498,499,5,110,
        0,0,499,500,5,95,0,0,500,501,5,114,0,0,501,502,5,101,0,0,502,503,
        5,115,0,0,503,504,5,117,0,0,504,505,5,108,0,0,505,506,5,116,0,0,
        506,110,1,0,0,0,507,508,5,97,0,0,508,509,5,100,0,0,509,510,5,118,
        0,0,510,511,5,101,0,0,511,512,5,110,0,0,512,513,5,116,0,0,513,514,
        5,117,0,0,514,515,5,114,0,0,515,516,5,101,0,0,516,517,5,95,0,0,517,
        518,5,108,0,0,518,519,5,111,0,0,519,520,5,103,0,0,520,112,1,0,0,
        0,521,522,5,109,0,0,522,523,5,101,0,0,523,524,5,115,0,0,524,525,
        5,115,0,0,525,526,5,97,0,0,526,527,5,103,0,0,527,528,5,101,0,0,528,
        529,5,95,0,0,529,530,5,83,0,0,530,531,5,119,0,0,531,532,5,105,0,
        0,532,533,5,116,0,0,533,534,5,99,0,0,534,535,5,104,0,0,535,536,5,
        84,0,0,536,537,5,97,0,0,537,538,5,108,0,0,538,539,5,107,0,0,539,
        114,1,0,0,0,540,541,5,109,0,0,541,542,5,101,0,0,542,543,5,115,0,
        0,543,544,5,115,0,0,544,545,5,97,0,0,545,546,5,103,0,0,546,547,5,
        101,0,0,547,548,5,95,0,0,548,549,5,83,0,0,549,550,5,119,0,0,550,
        551,5,105,0,0,551,552,5,116,0,0,552,553,5,99,0,0,553,554,5,104,0,
        0,554,555,5,77,0,0,555,556,5,111,0,0,556,557,5,110,0,0,557,558,5,
        111,0,0,558,559,5,108,0,0,559,560,5,111,0,0,560,561,5,103,0,0,561,
        562,5,117,0,0,562,563,5,101,0,0,563,116,1,0,0,0,564,565,5,119,0,
        0,565,566,5,104,0,0,566,567,5,105,0,0,567,568,5,108,0,0,568,569,
        5,101,0,0,569,118,1,0,0,0,570,571,5,102,0,0,571,572,5,111,0,0,572,
        573,5,114,0,0,573,120,1,0,0,0,574,575,5,91,0,0,575,122,1,0,0,0,576,
        577,5,93,0,0,577,124,1,0,0,0,578,583,5,39,0,0,579,582,3,185,92,0,
        580,582,8,0,0,0,581,579,1,0,0,0,581,580,1,0,0,0,582,585,1,0,0,0,
        583,581,1,0,0,0,583,584,1,0,0,0,584,586,1,0,0,0,585,583,1,0,0,0,
        586,597,5,39,0,0,587,592,5,34,0,0,588,591,3,185,92,0,589,591,8,1,
        0,0,590,588,1,0,0,0,590,589,1,0,0,0,591,594,1,0,0,0,592,590,1,0,
        0,0,592,593,1,0,0,0,593,595,1,0,0,0,594,592,1,0,0,0,595,597,5,34,
        0,0,596,578,1,0,0,0,596,587,1,0,0,0,597,126,1,0,0,0,598,602,3,133,
        66,0,599,602,3,135,67,0,600,602,3,137,68,0,601,598,1,0,0,0,601,599,
        1,0,0,0,601,600,1,0,0,0,602,128,1,0,0,0,603,604,5,99,0,0,604,605,
        5,111,0,0,605,606,5,114,0,0,606,607,5,111,0,0,607,130,1,0,0,0,608,
        609,5,100,0,0,609,610,5,101,0,0,610,611,5,102,0,0,611,132,1,0,0,
        0,612,613,5,102,0,0,613,614,5,111,0,0,614,615,5,114,0,0,615,616,
        5,95,0,0,616,617,5,97,0,0,617,618,5,99,0,0,618,619,5,116,0,0,619,
        620,5,111,0,0,620,621,5,114,0,0,621,134,1,0,0,0,622,623,5,102,0,
        0,623,624,5,111,0,0,624,625,5,114,0,0,625,626,5,95,0,0,626,627,5,
        111,0,0,627,628,5,98,0,0,628,629,5,106,0,0,629,630,5,101,0,0,630,
        631,5,99,0,0,631,632,5,116,0,0,632,136,1,0,0,0,633,634,5,102,0,0,
        634,635,5,111,0,0,635,636,5,114,0,0,636,637,5,95,0,0,637,638,5,112,
        0,0,638,639,5,101,0,0,639,640,5,114,0,0,640,641,5,102,0,0,641,642,
        5,111,0,0,642,643,5,114,0,0,643,644,5,109,0,0,644,645,5,101,0,0,
        645,646,5,114,0,0,646,138,1,0,0,0,647,648,5,97,0,0,648,649,5,108,
        0,0,649,650,5,105,0,0,650,651,5,97,0,0,651,652,5,115,0,0,652,140,
        1,0,0,0,653,654,5,112,0,0,654,655,5,114,0,0,655,656,5,101,0,0,656,
        657,5,118,0,0,657,658,5,105,0,0,658,659,5,111,0,0,659,660,5,117,
        0,0,660,661,5,115,0,0,661,142,1,0,0,0,662,663,5,80,0,0,663,664,5,
        111,0,0,664,665,5,115,0,0,665,666,5,105,0,0,666,667,5,116,0,0,667,
        668,5,105,0,0,668,669,5,111,0,0,669,670,5,110,0,0,670,144,1,0,0,
        0,671,672,3,205,102,0,672,146,1,0,0,0,673,674,7,2,0,0,674,675,3,
        205,102,0,675,148,1,0,0,0,676,677,7,3,0,0,677,678,3,205,102,0,678,
        150,1,0,0,0,679,684,3,153,76,0,680,684,3,155,77,0,681,684,3,157,
        78,0,682,684,3,159,79,0,683,679,1,0,0,0,683,680,1,0,0,0,683,681,
        1,0,0,0,683,682,1,0,0,0,684,152,1,0,0,0,685,687,5,45,0,0,686,685,
        1,0,0,0,686,687,1,0,0,0,687,688,1,0,0,0,688,692,3,187,93,0,689,691,
        3,189,94,0,690,689,1,0,0,0,691,694,1,0,0,0,692,690,1,0,0,0,692,693,
        1,0,0,0,693,704,1,0,0,0,694,692,1,0,0,0,695,697,5,45,0,0,696,695,
        1,0,0,0,696,697,1,0,0,0,697,699,1,0,0,0,698,700,5,48,0,0,699,698,
        1,0,0,0,700,701,1,0,0,0,701,699,1,0,0,0,701,702,1,0,0,0,702,704,
        1,0,0,0,703,686,1,0,0,0,703,696,1,0,0,0,704,154,1,0,0,0,705,707,
        5,45,0,0,706,705,1,0,0,0,706,707,1,0,0,0,707,708,1,0,0,0,708,709,
        5,48,0,0,709,711,7,4,0,0,710,712,3,191,95,0,711,710,1,0,0,0,712,
        713,1,0,0,0,713,711,1,0,0,0,713,714,1,0,0,0,714,156,1,0,0,0,715,
        717,5,45,0,0,716,715,1,0,0,0,716,717,1,0,0,0,717,718,1,0,0,0,718,
        719,5,48,0,0,719,721,7,5,0,0,720,722,3,193,96,0,721,720,1,0,0,0,
        722,723,1,0,0,0,723,721,1,0,0,0,723,724,1,0,0,0,724,158,1,0,0,0,
        725,727,5,45,0,0,726,725,1,0,0,0,726,727,1,0,0,0,727,728,1,0,0,0,
        728,729,5,48,0,0,729,731,7,6,0,0,730,732,3,195,97,0,731,730,1,0,
        0,0,732,733,1,0,0,0,733,731,1,0,0,0,733,734,1,0,0,0,734,160,1,0,
        0,0,735,736,5,40,0,0,736,162,1,0,0,0,737,738,5,41,0,0,738,164,1,
        0,0,0,739,740,5,44,0,0,740,166,1,0,0,0,741,742,5,58,0,0,742,168,
        1,0,0,0,743,744,5,43,0,0,744,170,1,0,0,0,745,746,5,64,0,0,746,172,
        1,0,0,0,747,748,5,167,0,0,748,174,1,0,0,0,749,750,5,123,0,0,750,
        176,1,0,0,0,751,752,5,125,0,0,752,178,1,0,0,0,753,754,5,46,0,0,754,
        755,5,53,0,0,755,180,1,0,0,0,756,761,3,203,101,0,757,761,3,201,100,
        0,758,761,3,197,98,0,759,761,3,199,99,0,760,756,1,0,0,0,760,757,
        1,0,0,0,760,758,1,0,0,0,760,759,1,0,0,0,761,762,1,0,0,0,762,763,
        6,90,0,0,763,182,1,0,0,0,764,765,9,0,0,0,765,184,1,0,0,0,766,767,
        5,92,0,0,767,768,9,0,0,0,768,186,1,0,0,0,769,770,7,7,0,0,770,188,
        1,0,0,0,771,772,7,8,0,0,772,190,1,0,0,0,773,774,7,9,0,0,774,192,
        1,0,0,0,775,776,7,10,0,0,776,194,1,0,0,0,777,778,7,11,0,0,778,196,
        1,0,0,0,779,781,7,12,0,0,780,779,1,0,0,0,781,782,1,0,0,0,782,780,
        1,0,0,0,782,783,1,0,0,0,783,198,1,0,0,0,784,786,5,92,0,0,785,787,
        3,197,98,0,786,785,1,0,0,0,786,787,1,0,0,0,787,793,1,0,0,0,788,790,
        5,13,0,0,789,788,1,0,0,0,789,790,1,0,0,0,790,791,1,0,0,0,791,794,
        5,10,0,0,792,794,2,12,13,0,793,789,1,0,0,0,793,792,1,0,0,0,794,200,
        1,0,0,0,795,796,5,47,0,0,796,797,5,42,0,0,797,801,1,0,0,0,798,800,
        9,0,0,0,799,798,1,0,0,0,800,803,1,0,0,0,801,802,1,0,0,0,801,799,
        1,0,0,0,802,807,1,0,0,0,803,801,1,0,0,0,804,805,5,42,0,0,805,808,
        5,47,0,0,806,808,5,0,0,1,807,804,1,0,0,0,807,806,1,0,0,0,808,202,
        1,0,0,0,809,810,5,47,0,0,810,811,5,47,0,0,811,815,1,0,0,0,812,814,
        8,13,0,0,813,812,1,0,0,0,814,817,1,0,0,0,815,813,1,0,0,0,815,816,
        1,0,0,0,816,204,1,0,0,0,817,815,1,0,0,0,818,822,7,14,0,0,819,821,
        7,15,0,0,820,819,1,0,0,0,821,824,1,0,0,0,822,820,1,0,0,0,822,823,
        1,0,0,0,823,206,1,0,0,0,824,822,1,0,0,0,29,0,212,581,583,590,592,
        596,601,683,686,692,696,701,703,706,713,716,723,726,733,760,782,
        786,789,793,801,807,815,822,1,6,0,0
    ]

class ExplorerScriptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    CTX_TYPE = 2
    OP_FALSE = 3
    OP_TRUE = 4
    ASSIGN = 5
    OPEN_SHARP = 6
    CLOSE_SHARP = 7
    OP_EQ = 8
    OP_LE = 9
    OP_GE = 10
    OP_NEQ = 11
    OP_AND = 12
    OP_XOR = 13
    OP_BICH = 14
    OP_MINUS = 15
    OP_PLUS = 16
    OP_MULTIPLY = 17
    OP_DIVIDE = 18
    OR = 19
    NOT = 20
    JUMP = 21
    CALL = 22
    IMPORT = 23
    MACRO = 24
    IF = 25
    ELSEIF = 26
    ELSE = 27
    FOREVER = 28
    WITH = 29
    SWITCH = 30
    RETURN = 31
    END = 32
    HOLD = 33
    CONTINUE = 34
    BREAK = 35
    BREAK_LOOP = 36
    ACTOR = 37
    OBJECT = 38
    PERFORMER = 39
    VALUE = 40
    DEBUG = 41
    EDIT = 42
    VARIATION = 43
    RANDOM = 44
    SECTOR = 45
    DUNGEON_MODE = 46
    MENU2 = 47
    MENU = 48
    CASE = 49
    DEFAULT = 50
    CLEAR = 51
    RESET = 52
    INIT = 53
    SCN = 54
    DUNGEON_RESULT = 55
    ADVENTURE_LOG = 56
    MESSAGE_SWITCH_TALK = 57
    MESSAGE_SWITCH_MONOLOGUE = 58
    WHILE = 59
    FOR = 60
    OPEN_BRACKET = 61
    CLOSE_BRACKET = 62
    STRING_LITERAL = 63
    FOR_TARGET = 64
    CORO = 65
    DEF = 66
    FOR_ACTOR = 67
    FOR_OBJECT = 68
    FOR_PERFORMER = 69
    ALIAS = 70
    PREVIOUS = 71
    POSITION = 72
    IDENTIFIER = 73
    VARIABLE = 74
    MACRO_CALL = 75
    INTEGER = 76
    DECIMAL_INTEGER = 77
    OCT_INTEGER = 78
    HEX_INTEGER = 79
    BIN_INTEGER = 80
    OPEN_PAREN = 81
    CLOSE_PAREN = 82
    COMMA = 83
    COLON = 84
    PLUS = 85
    AT = 86
    PARAGRAPH = 87
    OPEN_BRACE = 88
    CLOSE_BRACE = 89
    POINT_FIVE = 90
    SKIP_ = 91
    UNKNOWN_CHAR = 92

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'FALSE'", "'TRUE'", "'='", "'<'", "'>'", "'=='", "'<='", 
            "'>='", "'!='", "'&'", "'^'", "'&<<'", "'-='", "'+='", "'*='", 
            "'/='", "'||'", "'not'", "'jump'", "'call'", "'import'", "'macro'", 
            "'if'", "'elseif'", "'else'", "'forever'", "'with'", "'switch'", 
            "'return'", "'end'", "'hold'", "'continue'", "'break'", "'break_loop'", 
            "'actor'", "'object'", "'performer'", "'value'", "'debug'", 
            "'edit'", "'variation'", "'random'", "'sector'", "'dungeon_mode'", 
            "'menu2'", "'menu'", "'case'", "'default'", "'clear'", "'reset'", 
            "'init'", "'scn'", "'dungeon_result'", "'adventure_log'", "'message_SwitchTalk'", 
            "'message_SwitchMonologue'", "'while'", "'for'", "'['", "']'", 
            "'coro'", "'def'", "'for_actor'", "'for_object'", "'for_performer'", 
            "'alias'", "'previous'", "'Position'", "'('", "')'", "','", 
            "':'", "'+'", "'@'", "'\\u00A7'", "'{'", "'}'", "'.5'" ]

    symbolicNames = [ "<INVALID>",
            "CTX_TYPE", "OP_FALSE", "OP_TRUE", "ASSIGN", "OPEN_SHARP", "CLOSE_SHARP", 
            "OP_EQ", "OP_LE", "OP_GE", "OP_NEQ", "OP_AND", "OP_XOR", "OP_BICH", 
            "OP_MINUS", "OP_PLUS", "OP_MULTIPLY", "OP_DIVIDE", "OR", "NOT", 
            "JUMP", "CALL", "IMPORT", "MACRO", "IF", "ELSEIF", "ELSE", "FOREVER", 
            "WITH", "SWITCH", "RETURN", "END", "HOLD", "CONTINUE", "BREAK", 
            "BREAK_LOOP", "ACTOR", "OBJECT", "PERFORMER", "VALUE", "DEBUG", 
            "EDIT", "VARIATION", "RANDOM", "SECTOR", "DUNGEON_MODE", "MENU2", 
            "MENU", "CASE", "DEFAULT", "CLEAR", "RESET", "INIT", "SCN", 
            "DUNGEON_RESULT", "ADVENTURE_LOG", "MESSAGE_SWITCH_TALK", "MESSAGE_SWITCH_MONOLOGUE", 
            "WHILE", "FOR", "OPEN_BRACKET", "CLOSE_BRACKET", "STRING_LITERAL", 
            "FOR_TARGET", "CORO", "DEF", "FOR_ACTOR", "FOR_OBJECT", "FOR_PERFORMER", 
            "ALIAS", "PREVIOUS", "POSITION", "IDENTIFIER", "VARIABLE", "MACRO_CALL", 
            "INTEGER", "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", 
            "BIN_INTEGER", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", 
            "PLUS", "AT", "PARAGRAPH", "OPEN_BRACE", "CLOSE_BRACE", "POINT_FIVE", 
            "SKIP_", "UNKNOWN_CHAR" ]

    ruleNames = [ "T__0", "CTX_TYPE", "OP_FALSE", "OP_TRUE", "ASSIGN", "OPEN_SHARP", 
                  "CLOSE_SHARP", "OP_EQ", "OP_LE", "OP_GE", "OP_NEQ", "OP_AND", 
                  "OP_XOR", "OP_BICH", "OP_MINUS", "OP_PLUS", "OP_MULTIPLY", 
                  "OP_DIVIDE", "OR", "NOT", "JUMP", "CALL", "IMPORT", "MACRO", 
                  "IF", "ELSEIF", "ELSE", "FOREVER", "WITH", "SWITCH", "RETURN", 
                  "END", "HOLD", "CONTINUE", "BREAK", "BREAK_LOOP", "ACTOR", 
                  "OBJECT", "PERFORMER", "VALUE", "DEBUG", "EDIT", "VARIATION", 
                  "RANDOM", "SECTOR", "DUNGEON_MODE", "MENU2", "MENU", "CASE", 
                  "DEFAULT", "CLEAR", "RESET", "INIT", "SCN", "DUNGEON_RESULT", 
                  "ADVENTURE_LOG", "MESSAGE_SWITCH_TALK", "MESSAGE_SWITCH_MONOLOGUE", 
                  "WHILE", "FOR", "OPEN_BRACKET", "CLOSE_BRACKET", "STRING_LITERAL", 
                  "FOR_TARGET", "CORO", "DEF", "FOR_ACTOR", "FOR_OBJECT", 
                  "FOR_PERFORMER", "ALIAS", "PREVIOUS", "POSITION", "IDENTIFIER", 
                  "VARIABLE", "MACRO_CALL", "INTEGER", "DECIMAL_INTEGER", 
                  "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "OPEN_PAREN", 
                  "CLOSE_PAREN", "COMMA", "COLON", "PLUS", "AT", "PARAGRAPH", 
                  "OPEN_BRACE", "CLOSE_BRACE", "POINT_FIVE", "SKIP_", "UNKNOWN_CHAR", 
                  "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", "DIGIT", "OCT_DIGIT", 
                  "HEX_DIGIT", "BIN_DIGIT", "SPACES", "LINE_JOINING", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "IDENTIFIER_BASE" ]

    grammarFileName = "ExplorerScript.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


