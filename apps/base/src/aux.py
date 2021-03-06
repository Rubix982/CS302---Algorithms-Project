'''csv reader, python'''
from apps.base.src.word_break import wordBreak
from apps.base.src.shortest_common_supersequence import superSeqSelection
from apps.base.src.rod_cutting import rodCuttingTopDown
from apps.base.src.partition import findPartitionDynamicProgramming
from apps.base.src.matrix_chain_multiplication import matrixChainOrderSelection
from apps.base.src.longest_common_subsequence import longestCommonSubsequenceSelection
from apps.base.src.lis import longestIncreasingSubsequence
from apps.base.src.levenshtein_distance import levenshteinDynamic
from apps.base.src.knapsack_0_1 import knapsackSelection
from apps.base.src.coin_change_making import countSelection
import csv
import requests
import time

'''Algorithms'''

'''Datasets'''
dataset_0 = [
    ['ALSMIAISSALAIISUFFILIUSLASAFUIISULSLIIFLAMIUSIFALILIMFALASAMLISAIFLILMLIASMAFLSIUIAISMILMAISLSIMAFS',
     'FSUIIAIUSIMASLMILAISMMLIASAMLISALSIMISALMSLAMIALSMUILALMILUSALUSMLIILASMLUALSLAIMSFLLLISISILMASIILFU'],
    ['LUSMAUMLISALSLMLUSALSLSLSLAUMUSLASLMLMASUSLAMLLASUAMLSLAUUMIASALILMUILLSUAMAULLSIMLMSASULISMULAILL',
     'AMALMLUASLULSAAMLAULLAASMSULAULASLLMMAUSALLMASLMALUSAIUMSLAALLUSAMIAAMAALSIMILUSAAUULAAUAMLSMASLUL'],
    ['SMAUMLISSSAUULAAUASALAIISUMLSMASLALAUMUSLAFUMUSLASLMLMASUSUIISULSLIMLMSASSIIUSIMASLMILMAFLSIMAS',
     'SLAALLUSAMIAAMAALSIMAIUSIMSISILMASIILASIULSAAMLAULLAASMSULAULSLMILAISMMLIASAMALSMIAISSALASLSALILIML'],
    ['LAFUMIAISIUSIMSISILMASIISAAMLAULLAASMALAIUISALSLMLUSAIAIUSIMASLMILAISMMIMLMLUIAISMISLASL',
     'AISUMILAISMMAUIIAIUSIIUSIMMAFLSIAASMLUASLASLULSAAMLAAASIUIASAMLISALLSAALSMIAISSALALIILASSIMIMLMSAILUSAAUSLS'],
    ['IIAIISUMSLSLMLFFILAIISUFLIULSLMLUSSISILMASLAUSUSAAMLALAUMIUSIMSMIMLMUMLSIUSILSIUSLSIUSMSMIMLMA',
     'ISAISLSIMMAUILAULIMLAULLAMAFASIIAIUAISMMAULSAAMLIASLMIAMAAIUSIIUSSMMLIASAMAULSUSAAUSMSIMIMLIAISLIAMLSMASM'],
    ['MHUATMHDHUHTMHTMHUADDAHMHTHDAMUDMDHUHATTHTMHTHAMUDAUHDMDTHUAHMTHDHHDAUTMAHUTUAMHDHUHHAAHMUAHTUD',
     'TUTMDTHDTAUHDHMTDHAUMHUHAHDMUTHHAMHTUDHMTAHMUDTMHMUHDATHHAUHTDAHAUTHMDAUHTDHHUAMMTHUDMHAUADTAHDUMHHHAHDHM'],
    ['ATHMTHMHUHADTHDUHTAMDHMUHTAAHTUHDMDHMUAHTHAUMHDTADUHMUDMUHHDUAHTMUHADHUHMDHTAMTAHATDUMHTHDH',
     'DUUAUMTHDTHUMTUAHDUDAUMTTDMAUHUHHTUADUMUADMUMHUTUUDTUTDUMAUHHAMDATTATUMHUDUHDAMUHHDTUAADUMHUTMUMTDAUHUUAM'],
    ['ADAUHDMTUDUHATMUDUTAMHUDUTMUHAHUTAMDUMUTAHUDHUDUMTAMUDHUTAHTUMADUDUTHMUAAUMUTDHDUHUMTUMUHT',
     'AUMTUHDTDUUDAHTMUUTUMDAHHUMTUDADUMTHAUAUMUHTDAHTUDUMAUMHUDTDUMTAUHHUMDTAUMUHUDTATUHDAMUUTADHMUMUTUDAHAUTDHMAU'],
    ['MHTUDAUTMUADHTMUUMDHATUDTAHUMUHTUAMDUMHUTDAUTADHUMUUDMUTHAUTUADMHMDHUATUDUAUHMTDMHUTUAUHDTMUAH',
     'HMUMUATDUADTUTMUADTUADAUMTUHDUTMHUMUHAHDUAUHMTHUATMDUHUAMUDTHUAMUTDHTUAMUDHUADUMTsHTUADUMDMHUHUDUTA'],
    ['LSIISUFLAHUMUHUTMUHAMLSALSLSIMSISIMLUHATTHTUFUMUSAMLSLDUAHTMAUSAUTAMHUAIUSDUFFUHMDHILDMHUTUAII',
     'DUMTUAHDUTDUMDAHHUMAMAUMHUHAIAAMAALSIMAMHUTUAAMLAULUDTDDUAILAMLISALLSLMILIUSIIAUATMDUHUAMUADTUMAALSIHTM'],
]
dataset_1 = [
    ['ALSMIAISSALAIISUFFILIUSLASAFUIISULSLIIFLAMIUSIFALILIMFALASAMLISAIFLILMLIASMAFLSIUIAISMILMAISLSIMAFS',
     'FSUIIAIUSIMASLMILAISMMLIASAMLISALSIMISALMSLAMIALSMUILALMILUSALUSMLIILASMLUALSLAIMSFLLLISISILMASIILFU'],
    ['LUSMAUMLISALSLMLUSALSLSLSLAUMUSLASLMLMASUSLAMLLASUAMLSLAUUMIASALILMUILLSUAMAULLSIMLMSASULISMULAILL',
     'AMALMLUASLULSAAMLAULLAASMSULAULASLLMMAUSALLMASLMALUSAIUMSLAALLUSAMIAAMAALSIMILUSAAUULAAUAMLSMASLUL'],
    ['SMAUMLISSSAUULAAUASALAIISUMLSMASLALAUMUSLAFUMUSLASLMLMASUSUIISULSLIMLMSASSIIUSIMASLMILMAFLSIMAS',
     "SLAALLUSAMIAAMAALSIMAIUSIMSISILMASIILASIULSAAMLAULLAASMSULAULSLMILAISMMLIASAMALSMIAISSALASLSALILIML"],
    ['LAFUMIAISIUSIMSISILMASIISAAMLAULLAASMALAIUISALSLMLUSAIAIUSIMASLMILAISMMIMLMLUIAISMISLASL',
     'AISUMILAISMMAUIIAIUSIIUSIMMAFLSIAASMLUASLASLULSAAMLAAASIUIASAMLISALLSAALSMIAISSALALIILASSIMIMLMSAILUSAAUSLS'],
    ['IIAIISUMSLSLMLFFILAIISUFLIULSLMLUSSISILMASLAUSUSAAMLALAUMIUSIMSMIMLMUMLSIUSILSIUSLSIUSMSMIMLMA',
     'ISAISLSIMMAUILAULIMLAULLAMAFASIIAIUAISMMAULSAAMLIASLMIAMAAIUSIIUSSMMLIASAMAULSUSAAUSMSIMIMLIAISLIAMLSMASM'],
    ['MHUATMHDHUHTMHTMHUADDAHMHTHDAMUDMDHUHATTHTMHTHAMUDAUHDMDTHUAHMTHDHHDAUTMAHUTUAMHDHUHHAAHMUAHTUD',
     'TUTMDTHDTAUHDHMTDHAUMHUHAHDMUTHHAMHTUDHMTAHMUDTMHMUHDATHHAUHTDAHAUTHMDAUHTDHHUAMMTHUDMHAUADTAHDUMHHHAHDHM'],
    ['ATHMTHMHUHADTHDUHTAMDHMUHTAAHTUHDMDHMUAHTHAUMHDTADUHMUDMUHHDUAHTMUHADHUHMDHTAMTAHATDUMHTHDH',
     'DUUAUMTHDTHUMTUAHDUDAUMTTDMAUHUHHTUADUMUADMUMHUTUUDTUTDUMAUHHAMDATTATUMHUDUHDAMUHHDTUAADUMHUTMUMTDAUHUUAM'],
    ['ADAUHDMTUDUHATMUDUTAMHUDUTMUHAHUTAMDUMUTAHUDHUDUMTAMUDHUTAHTUMADUDUTHMUAAUMUTDHDUHUMTUMUHT',
     'AUMTUHDTDUUDAHTMUUTUMDAHHUMTUDADUMTHAUAUMUHTDAHTUDUMAUMHUDTDUMTAUHHUMDTAUMUHUDTATUHDAMUUTADHMUMUTUDAHAUTDHMAU'],
    ['MHTUDAUTMUADHTMUUMDHATUDTAHUMUHTUAMDUMHUTDAUTADHUMUUDMUTHAUTUADMHMDHUATUDUAUHMTDMHUTUAUHDTMUAH',
     'HMUMUATDUADTUTMUADTUADAUMTUHDUTMHUMUHAHDUAUHMTHUATMDUHUAMUDTHUAMUTDHTUAMUDHUADUMTsHTUADUMDMHUHUDUTA'],
    ['LSIISUFLAHUMUHUTMUHAMLSALSLSIMSISIMLUHATTHTUFUMUSAMLSLDUAHTMAUSAUTAMHUAIUSDUFFUHMDHILDMHUTUAII',
     'DUMTUAHDUTDUMDAHHUMAMAUMHUHAIAAMAALSIMAMHUTUAAMLAULUDTDDUAILAMLISALLSLMILIUSIIAUATMDUHUAMUADTUMAALSIHTM'],
]
dataset_2 = [
    ['ALSMIAISSALAIISUFFILIUSLASAFUIISULSLIIFLAMIUSIFALILIMFALASAMLISAIFLILMLIASMAFLSIUIAISMILMAISLSIMAFS',
     'FSUIIAIUSIMASLMILAISMMLIASAMLISALSIMISALMSLAMIALSMUILALMILUSALUSMLIILASMLUALSLAIMSFLLLISISILMASIILFU'],
    ['LUSMAUMLISALSLMLUSALSLSLSLAUMUSLASLMLMASUSLAMLLASUAMLSLAUUMIASALILMUILLSUAMAULLSIMLMSASULISMULAILL',
     'AMALMLUASLULSAAMLAULLAASMSULAULASLLMMAUSALLMASLMALUSAIUMSLAALLUSAMIAAMAALSIMILUSAAUULAAUAMLSMASLUL'],
    ['SMAUMLISSSAUULAAUASALAIISUMLSMASLALAUMUSLAFUMUSLASLMLMASUSUIISULSLIMLMSASSIIUSIMASLMILMAFLSIMAS',
     'SLAALLUSAMIAAMAALSIMAIUSIMSISILMASIILASIULSAAMLAULLAASMSULAULSLMILAISMMLIASAMALSMIAISSALASLSALILIML'],
    ['LAFUMIAISIUSIMSISILMASIISAAMLAULLAASMALAIUISALSLMLUSAIAIUSIMASLMILAISMMIMLMLUIAISMISLASL',
     'AISUMILAISMMAUIIAIUSIIUSIMMAFLSIAASMLUASLASLULSAAMLAAASIUIASAMLISALLSAALSMIAISSALALIILASSIMIMLMSAILUSAAUSLS'],
    ['IIAIISUMSLSLMLFFILAIISUFLIULSLMLUSSISILMASLAUSUSAAMLALAUMIUSIMSMIMLMUMLSIUSILSIUSLSIUSMSMIMLMA',
     'ISAISLSIMMAUILAULIMLAULLAMAFASIIAIUAISMMAULSAAMLIASLMIAMAAIUSIIUSSMMLIASAMAULSUSAAUSMSIMIMLIAISLIAMLSMASM'],
    ['MHUATMHDHUHTMHTMHUADDAHMHTHDAMUDMDHUHATTHTMHTHAMUDAUHDMDTHUAHMTHDHHDAUTMAHUTUAMHDHUHHAAHMUAHTUD',
     'TUTMDTHDTAUHDHMTDHAUMHUHAHDMUTHHAMHTUDHMTAHMUDTMHMUHDATHHAUHTDAHAUTHMDAUHTDHHUAMMTHUDMHAUADTAHDUMHHHAHDHM'],
    ['ATHMTHMHUHADTHDUHTAMDHMUHTAAHTUHDMDHMUAHTHAUMHDTADUHMUDMUHHDUAHTMUHADHUHMDHTAMTAHATDUMHTHDH',
     'DUUAUMTHDTHUMTUAHDUDAUMTTDMAUHUHHTUADUMUADMUMHUTUUDTUTDUMAUHHAMDATTATUMHUDUHDAMUHHDTUAADUMHUTMUMTDAUHUUAM'],
    ['ADAUHDMTUDUHATMUDUTAMHUDUTMUHAHUTAMDUMUTAHUDHUDUMTAMUDHUTAHTUMADUDUTHMUAAUMUTDHDUHUMTUMUHT',
     'AUMTUHDTDUUDAHTMUUTUMDAHHUMTUDADUMTHAUAUMUHTDAHTUDUMAUMHUDTDUMTAUHHUMDTAUMUHUDTATUHDAMUUTADHMUMUTUDAHAUTDHMAU'],
    ['MHTUDAUTMUADHTMUUMDHATUDTAHUMUHTUAMDUMHUTDAUTADHUMUUDMUTHAUTUADMHMDHUATUDUAUHMTDMHUTUAUHDTMUAH',
     'HMUMUATDUADTUTMUADTUADAUMTUHDUTMHUMUHAHDUAUHMTHUATMDUHUAMUDTHUAMUTDHTUAMUDHUADUMTsHTUADUMDMHUHUDUTA'],
    ['LSIISUFLAHUMUHUTMUHAMLSALSLSIMSISIMLUHATTHTUFUMUSAMLSLDUAHTMAUSAUTAMHUAIUSDUFFUHMDHILDMHUTUAII',
     'DUMTUAHDUTDUMDAHHUMAMAUMHUHAIAAMAALSIMAMHUTUAAMLAULUDTDDUAILAMLISALLSLMILIUSIIAUATMDUHUAMUADTUMAALSIHTM'],
]
dataset_3 = [
    [25, 84, 83, 71, 59, 82, 70, 67, 41, 14, 53, 80, 99, 84, 81, 47, 92, 90, 83, 82, 21, 100, 100, 69, 26, 27, 97, 32, 89, 13, 0, 71, 88, 50, 42, 15, 16, 64, 28, 19, 91, 59, 0, 15, 88, 23, 52, 2,
        99, 17, 52, 40, 60, 84, 18, 7, 0, 65, 27, 62, 7, 32, 66, 45, 28, 19, 21, 66, 12, 37, 71, 100, 92, 18, 83, 15, 5, 89, 75, 36, 41, 40, 68, 30, 32, 0, 54, 90, 68, 38, 0, 81, 58, 94, 57, 35, 49],
    [44, 64, 61, 2, 29, 1, 50, 75, 47, 54, 46, 95, 57, 55, 35, 3, 97, 74, 81, 35, 36, 56, 76, 54, 37, 94, 4, 32, 19, 88, 9, 87, 53, 27, 100, 64, 13, 84, 15, 16, 25, 50, 95, 5, 10, 43, 42, 9, 10,
        20, 9, 87, 84, 5, 36, 32, 50, 41, 98, 2, 13, 48, 46, 55, 79, 83, 81, 60, 50, 21, 81, 30, 3, 8, 99, 10, 85, 10, 25, 86, 58, 27, 25, 33, 62, 1, 60, 16, 82, 12, 74, 90, 1, 5, 91, 23, 76, 53],
    [76, 23, 43, 46, 90, 22, 20, 15, 34, 27, 31, 98, 25, 50, 80, 70, 8, 78, 36, 100, 70, 89, 70, 21, 33, 62, 9, 57, 79, 62, 77, 61, 39, 69, 81, 34, 40, 33, 20, 45, 77, 40, 81, 80, 17, 52, 93, 93, 58, 45,
        33, 87, 9, 44, 67, 72, 52, 11, 16, 54, 52, 97, 5, 18, 39, 18, 48, 26, 89, 21, 74, 58, 77, 51, 35, 100, 32, 72, 80, 46, 76, 45, 96, 47, 73, 57, 56, 96, 86, 3, 22, 7, 25, 27, 45, 95, 80, 79, 39, 29],
    [99, 56, 2, 23, 51, 95, 92, 73, 37, 43, 99, 21, 51, 73, 23, 17, 22, 73, 95, 18, 80, 97, 92, 99, 34, 100, 72, 12, 92, 15, 46, 51, 3, 62, 2, 57, 45, 79, 90, 51, 95, 4, 48, 17, 39, 93,
        31, 73, 100, 6, 44, 72, 45, 3, 30, 14, 53, 31, 62, 70, 38, 92, 83, 40, 0, 77, 14, 97, 34, 93, 41, 46, 39, 6, 39, 18, 49, 38, 48, 67, 66, 34, 42, 82, 64, 32, 2, 34, 27, 68, 55],
    [47, 27, 37, 1, 39, 42, 57, 66, 37, 17, 15, 48, 94, 96, 24, 25, 65, 55, 73, 35, 31, 13, 21, 69, 60, 24, 72, 3, 67, 71, 57, 42, 79, 8, 84, 19, 64, 60, 22, 5, 75, 100, 70, 68, 17, 92,
        97, 77, 21, 25, 37, 56, 56, 37, 32, 14, 40, 53, 10, 8, 84, 37, 79, 69, 48, 28, 14, 22, 89, 59, 44, 8, 73, 82, 93, 73, 0, 21, 66, 24, 13, 28, 38, 84, 53, 88, 14, 9, 96, 58, 96],
    [35, 16, 47, 14, 90, 53, 31, 70, 95, 63, 33, 86, 44, 56, 5, 14, 58, 55, 9, 89, 2, 28, 67, 88, 100, 59, 24, 78, 80, 33, 30, 73, 64, 13, 82, 69, 26, 79, 68, 8, 65, 44, 62, 81, 19,
        41, 19, 20, 9, 2, 96, 78, 17, 88, 65, 85, 84, 30, 72, 20, 82, 25, 62, 74, 61, 88, 46, 33, 43, 78, 83, 74, 20, 39, 7, 26, 30, 24, 39, 96, 100, 62, 12, 35, 98, 22, 86, 62, 99, 35],
    [7, 50, 60, 0, 0, 88, 30, 80, 27, 73, 14, 83, 36, 80, 59, 99, 26, 25, 15, 87, 27, 9, 48, 8, 63, 78, 77, 24, 90, 61, 49, 5, 29, 72, 31, 68, 41, 19, 8, 29, 98, 63, 12, 37, 7, 1, 22, 25, 36,
        22, 85, 5, 64, 96, 89, 40, 3, 56, 65, 70, 18, 92, 86, 27, 94, 82, 61, 100, 91, 61, 47, 63, 84, 62, 53, 5, 2, 19, 34, 60, 35, 3, 29, 52, 64, 39, 4, 55, 59, 49, 95, 40, 45, 95, 17, 92, 25, 20],
    [28, 60, 51, 97, 6, 79, 3, 73, 97, 81, 88, 21, 78, 39, 97, 69, 35, 90, 90, 56, 6, 31, 83, 54, 65, 96, 92, 20, 94, 35, 18, 67, 31, 57, 76, 10, 8, 40, 100, 98, 4, 69, 75, 14, 75, 73, 53, 36,
        15, 33, 63, 30, 27, 59, 75, 54, 97, 9, 73, 15, 30, 9, 17, 32, 70, 93, 81, 82, 6, 44, 56, 75, 73, 17, 88, 3, 36, 99, 63, 62, 16, 14, 81, 67, 33, 48, 11, 50, 92, 34, 46, 54, 36, 90, 76, 44],
    [16, 20, 70, 37, 16, 15, 20, 92, 44, 79, 49, 62, 3, 83, 84, 29, 11, 34, 81, 58, 22, 57, 38, 21, 12, 99, 17, 49, 36, 89, 43, 51, 60, 88, 69, 0, 17, 46, 35, 88, 93, 6, 29, 63, 97, 44, 37,
        67, 86, 38, 88, 9, 78, 9, 57, 91, 60, 41, 36, 81, 88, 3, 2, 22, 79, 82, 81, 82, 32, 95, 72, 94, 79, 19, 1, 5, 59, 100, 40, 5, 1, 12, 41, 83, 27, 49, 19, 53, 11, 75, 61, 85, 37, 62],
    [30, 30, 46, 91, 61, 28, 18, 7, 46, 53, 85, 79, 87, 53, 58, 25, 8, 100, 55, 55, 24, 23, 56, 99, 68, 43, 20, 71, 71, 0, 2, 74, 71, 73, 99, 22, 96, 85, 78, 93, 0, 21, 65, 38, 5, 82, 99, 92,
        60, 75, 97, 22, 67, 60, 100, 0, 48, 79, 77, 66, 35, 86, 93, 8, 19, 49, 62, 51, 57, 26, 98, 42, 68, 66, 2, 7, 80, 75, 94, 80, 90, 85, 60, 44, 55, 44, 63, 13, 100, 64, 71, 47, 6, 20, 15, 25],
]
dataset_4 = [
    [25, 84, 83, 71, 59, 82, 70, 67, 41, 14, 53, 80, 99, 84, 81, 47, 92, 90, 83, 82, 21, 100, 100, 69, 26, 27, 97, 32, 89, 13, 0, 71, 88, 50, 42, 15, 16, 64, 28, 19, 91, 59, 0, 15, 88, 23, 52, 2,
     99, 17, 52, 40, 60, 84, 18, 7, 0, 65, 27, 62, 7, 32, 66, 45, 28, 19, 21, 66, 12, 37, 71, 100, 92, 18, 83, 15, 5, 89, 75, 36, 41, 40, 68, 30, 32, 0, 54, 90, 68, 38, 0, 81, 58, 94, 57, 35, 49],
    [44, 64, 61, 2, 29, 1, 50, 75, 47, 54, 46, 95, 57, 55, 35, 3, 97, 74, 81, 35, 36, 56, 76, 54, 37, 94, 4, 32, 19, 88, 9, 87, 53, 27, 100, 64, 13, 84, 15, 16, 25, 50, 95, 5, 10, 43, 42, 9, 10,
     20, 9, 87, 84, 5, 36, 32, 50, 41, 98, 2, 13, 48, 46, 55, 79, 83, 81, 60, 50, 21, 81, 30, 3, 8, 99, 10, 85, 10, 25, 86, 58, 27, 25, 33, 62, 1, 60, 16, 82, 12, 74, 90, 1, 5, 91, 23, 76, 53],
    [76, 23, 43, 46, 90, 22, 20, 15, 34, 27, 31, 98, 25, 50, 80, 70, 8, 78, 36, 100, 70, 89, 70, 21, 33, 62, 9, 57, 79, 62, 77, 61, 39, 69, 81, 34, 40, 33, 20, 45, 77, 40, 81, 80, 17, 52, 93, 93, 58, 45,
     33, 87, 9, 44, 67, 72, 52, 11, 16, 54, 52, 97, 5, 18, 39, 18, 48, 26, 89, 21, 74, 58, 77, 51, 35, 100, 32, 72, 80, 46, 76, 45, 96, 47, 73, 57, 56, 96, 86, 3, 22, 7, 25, 27, 45, 95, 80, 79, 39, 29],
    [99, 56, 2, 23, 51, 95, 92, 73, 37, 43, 99, 21, 51, 73, 23, 17, 22, 73, 95, 18, 80, 97, 92, 99, 34, 100, 72, 12, 92, 15, 46, 51, 3, 62, 2, 57, 45, 79, 90, 51, 95, 4, 48, 17, 39, 93,
     31, 73, 100, 6, 44, 72, 45, 3, 30, 14, 53, 31, 62, 70, 38, 92, 83, 40, 0, 77, 14, 97, 34, 93, 41, 46, 39, 6, 39, 18, 49, 38, 48, 67, 66, 34, 42, 82, 64, 32, 2, 34, 27, 68, 55],
    [47, 27, 37, 1, 39, 42, 57, 66, 37, 17, 15, 48, 94, 96, 24, 25, 65, 55, 73, 35, 31, 13, 21, 69, 60, 24, 72, 3, 67, 71, 57, 42, 79, 8, 84, 19, 64, 60, 22, 5, 75, 100, 70, 68, 17, 92,
     97, 77, 21, 25, 37, 56, 56, 37, 32, 14, 40, 53, 10, 8, 84, 37, 79, 69, 48, 28, 14, 22, 89, 59, 44, 8, 73, 82, 93, 73, 0, 21, 66, 24, 13, 28, 38, 84, 53, 88, 14, 9, 96, 58, 96],
    [35, 16, 47, 14, 90, 53, 31, 70, 95, 63, 33, 86, 44, 56, 5, 14, 58, 55, 9, 89, 2, 28, 67, 88, 100, 59, 24, 78, 80, 33, 30, 73, 64, 13, 82, 69, 26, 79, 68, 8, 65, 44, 62, 81, 19,
     41, 19, 20, 9, 2, 96, 78, 17, 88, 65, 85, 84, 30, 72, 20, 82, 25, 62, 74, 61, 88, 46, 33, 43, 78, 83, 74, 20, 39, 7, 26, 30, 24, 39, 96, 100, 62, 12, 35, 98, 22, 86, 62, 99, 35],
    [7, 50, 60, 0, 0, 88, 30, 80, 27, 73, 14, 83, 36, 80, 59, 99, 26, 25, 15, 87, 27, 9, 48, 8, 63, 78, 77, 24, 90, 61, 49, 5, 29, 72, 31, 68, 41, 19, 8, 29, 98, 63, 12, 37, 7, 1, 22, 25, 36,
     22, 85, 5, 64, 96, 89, 40, 3, 56, 65, 70, 18, 92, 86, 27, 94, 82, 61, 100, 91, 61, 47, 63, 84, 62, 53, 5, 2, 19, 34, 60, 35, 3, 29, 52, 64, 39, 4, 55, 59, 49, 95, 40, 45, 95, 17, 92, 25, 20],
    [28, 60, 51, 97, 6, 79, 3, 73, 97, 81, 88, 21, 78, 39, 97, 69, 35, 90, 90, 56, 6, 31, 83, 54, 65, 96, 92, 20, 94, 35, 18, 67, 31, 57, 76, 10, 8, 40, 100, 98, 4, 69, 75, 14, 75, 73, 53, 36,
     15, 33, 63, 30, 27, 59, 75, 54, 97, 9, 73, 15, 30, 9, 17, 32, 70, 93, 81, 82, 6, 44, 56, 75, 73, 17, 88, 3, 36, 99, 63, 62, 16, 14, 81, 67, 33, 48, 11, 50, 92, 34, 46, 54, 36, 90, 76, 44],
    [16, 20, 70, 37, 16, 15, 20, 92, 44, 79, 49, 62, 3, 83, 84, 29, 11, 34, 81, 58, 22, 57, 38, 21, 12, 99, 17, 49, 36, 89, 43, 51, 60, 88, 69, 0, 17, 46, 35, 88, 93, 6, 29, 63, 97, 44, 37,
     67, 86, 38, 88, 9, 78, 9, 57, 91, 60, 41, 36, 81, 88, 3, 2, 22, 79, 82, 81, 82, 32, 95, 72, 94, 79, 19, 1, 5, 59, 100, 40, 5, 1, 12, 41, 83, 27, 49, 19, 53, 11, 75, 61, 85, 37, 62],
    [30, 30, 46, 91, 61, 28, 18, 7, 46, 53, 85, 79, 87, 53, 58, 25, 8, 100, 55, 55, 24, 23, 56, 99, 68, 43, 20, 71, 71, 0, 2, 74, 71, 73, 99, 22, 96, 85, 78, 93, 0, 21, 65, 38, 5, 82, 99, 92,
     60, 75, 97, 22, 67, 60, 100, 0, 48, 79, 77, 66, 35, 86, 93, 8, 19, 49, 62, 51, 57, 26, 98, 42, 68, 66, 2, 7, 80, 75, 94, 80, 90, 85, 60, 44, 55, 44, 63, 13, 100, 64, 71, 47, 6, 20, 15, 25],
]
dataset_5 = [
    [[57, 14], [75, 62], [32, 22], [42, 38], [27, 100], [96, 74], [73, 19], [17, 95], [98, 53], [36, 77], [76, 87], [51, 55], [64, 41], [67, 95], [10, 85], [54, 31], [94, 47], [73, 18], [69, 79], [36, 68], [41, 61], [10, 99], [56, 27], [97, 26], [64, 43], [11, 79], [85, 54], [81, 25], [88, 69], [
        41, 13], [87, 55], [44, 94], [56, 58], [49, 75], [32, 39], [34, 82], [72, 52], [77, 30], [41, 74], [69, 78], [90, 43], [16, 90], [25, 82], [64, 92], [66, 61], [67, 28], [91, 13], [19, 84], [26, 94], [18, 23], [73, 44], [25, 27], [83, 36], [73, 98], [97, 92], [43, 52], [21, 85], [98, 87]],
    [[41, 69], [20, 70], [84, 55], [82, 75], [65, 11], [96, 54], [10, 79], [60, 30], [64, 15], [64, 95], [
        80, 90], [59, 36], [48, 33], [41, 85], [94, 63], [98, 68], [50, 69], [44, 29], [61, 39], [97, 74]],
    [[84, 45], [81, 82], [74, 21], [86, 54], [32, 61], [43, 35], [81, 18], [82, 87], [12, 77], [65, 62], [91, 38], [64, 37], [19, 43], [82, 87], [96, 34], [98, 87], [51, 87], [14, 30], [81, 85], [64, 75], [88, 94], [89, 19], [58, 92], [53, 30], [57, 95], [67, 28], [79, 39], [94, 87], [97, 67], [72, 29], [23, 87], [19, 69], [19, 46], [96, 91], [84, 37], [33, 46], [64, 77], [84, 55], [99, 52], [100, 95], [57, 12], [32, 49], [64, 74], [27, 20], [82, 70], [48, 87], [72, 89], [52, 95], [
        84, 63], [57, 91], [88, 80], [90, 29], [90, 11], [13, 94], [12, 13], [17, 44], [94, 38], [69, 23], [81, 63], [58, 87], [89, 12], [38, 55], [59, 38], [61, 17], [32, 73], [16, 39], [16, 79], [80, 98], [72, 17], [40, 32], [63, 55], [99, 77], [51, 19], [51, 76], [58, 76], [25, 51], [65, 98], [61, 30], [74, 70], [56, 39], [57, 54], [19, 15], [76, 77], [24, 29], [49, 78], [99, 92], [26, 75], [94, 71], [83, 22], [91, 44], [25, 12], [84, 69], [64, 100], [40, 57], [16, 27], [72, 98]],
    [[82, 12], [35, 54], [64, 46], [40, 59], [72, 89], [26, 34], [27, 100], [58, 30], [41, 31], [33, 18], [15, 63], [59, 68], [
        13, 39], [67, 13], [48, 75], [44, 71], [59, 46], [12, 37], [35, 76], [78, 15], [40, 10], [78, 86], [84, 87], [31, 71]],
    [[80, 47], [69, 46], [27, 61], [36, 85], [78, 95], [97, 53], [89, 95], [32, 17], [19, 31], [41, 19], [51, 44], [18, 71], [84, 21], [35, 46], [49, 53], [62, 22], [48, 52], [51, 28], [88, 43], [42, 62], [65, 79], [98, 44], [57, 68], [26, 14], [83, 92], [23, 95], [
        57, 37], [69, 14], [59, 55], [76, 22], [98, 86], [15, 23], [96, 78], [71, 95], [54, 95], [72, 87], [26, 37], [51, 38], [17, 13], [83, 78], [48, 40], [17, 68], [89, 91], [32, 39], [85, 22], [96, 90], [11, 28], [22, 95], [67, 37], [89, 61], [43, 84], [58, 91], [19, 93]],
    [[18, 23], [17, 86], [11, 93], [81, 74], [17, 28], [33, 35], [34, 67], [
        65, 35], [98, 86], [48, 100], [18, 23], [50, 82], [89, 33], [91, 63]],
    [[35, 13], [96, 11], [64, 78], [40, 14], [56, 49], [40, 50], [86, 14], [88, 49], [74, 92], [76, 77], [82, 76], [11, 15], [26, 22], [66, 37], [
        10, 31], [59, 11], [60, 31], [26, 98], [16, 67], [35, 39], [62, 39], [17, 29], [82, 42], [23, 55], [10, 98], [72, 27], [74, 11], [45, 23]],
    [[82, 67], [83, 87], [50, 39], [81, 30], [32, 90], [83, 45], [46, 94], [41, 53], [98, 99], [41, 34], [27, 36], [60, 69], [90, 52], [89, 19], [88, 83], [24, 16], [83, 55], [51, 21], [42, 20], [
        32, 57], [19, 71], [49, 18], [54, 95], [67, 44], [18, 39], [21, 71], [13, 53], [33, 78], [13, 87], [70, 55], [64, 19], [56, 73], [28, 45], [61, 23], [89, 87], [98, 93], [67, 28], [56, 36], [52, 36]],
    [[92, 62], [89, 85], [84, 54], [83, 45], [41, 45], [25, 62], [10, 76], [89, 75], [78, 63], [32, 21], [81, 17], [72, 86], [42, 21], [49, 53], [64, 72], [11, 76], [21, 53], [56, 29], [65, 25], [49, 34], [34, 36], [72, 13], [35, 15], [70, 62], [
        57, 29], [41, 57], [38, 86], [65, 36], [35, 45], [64, 15], [89, 90], [89, 86], [65, 42], [89, 61], [33, 93], [92, 23], [21, 63], [36, 63], [10, 42], [66, 38], [100, 63], [49, 99], [26, 21], [33, 25], [72, 71], [72, 94], [49, 98], [24, 90], [78, 95]],
    [[32, 97], [10, 76], [66, 19], [44, 54], [97, 37], [10, 61], [27, 62], [65, 44], [48, 11], [91, 68], [10, 34], [33, 55], [64, 14], [74, 76], [24, 70], [84, 39], [29, 47], [12, 54], [56, 92], [50, 68], [98, 43], [44, 85], [50, 91], [19, 28], [26, 35], [100, 54], [77, 47], [33, 76], [97, 14], [26, 92], [81, 55], [89, 89], [64, 77], [28, 13], [72, 59], [60, 78], [64, 55], [56, 17], [96, 60], [96, 91], [59, 21], [77, 61], [81, 34], [
        85, 78], [33, 59], [94, 71], [30, 63], [33, 54], [26, 95], [88, 67], [90, 67], [57, 71], [90, 69], [67, 12], [72, 13], [90, 23], [83, 28], [34, 60], [56, 65], [80, 61], [45, 95], [17, 55], [11, 84], [60, 38], [43, 93], [58, 27], [27, 39], [94, 71], [72, 14], [29, 30], [53, 54], [56, 77], [80, 85], [74, 60], [74, 37], [66, 11], [76, 95], [36, 22], [32, 67], [56, 98], [32, 67], [72, 85], [35, 13], [65, 10], [92, 94], [80, 92]],
]
dataset_6 = [
    [[57, 14], [75, 62], [32, 22], [42, 38], [27, 100], [96, 74], [73, 19], [17, 95], [98, 53], [36, 77], [76, 87], [51, 55], [64, 41], [67, 95], [10, 85], [54, 31], [94, 47], [73, 18], [69, 79], [36, 68], [41, 61], [10, 99], [56, 27], [97, 26], [64, 43], [11, 79], [85, 54], [81, 25], [88, 69], [
        41, 13], [87, 55], [44, 94], [56, 58], [49, 75], [32, 39], [34, 82], [72, 52], [77, 30], [41, 74], [69, 78], [90, 43], [16, 90], [25, 82], [64, 92], [66, 61], [67, 28], [91, 13], [19, 84], [26, 94], [18, 23], [73, 44], [25, 27], [83, 36], [73, 98], [97, 92], [43, 52], [21, 85], [98, 87]],
    [[41, 69], [20, 70], [84, 55], [82, 75], [65, 11], [96, 54], [10, 79], [60, 30], [64, 15], [64, 95], [
     80, 90], [59, 36], [48, 33], [41, 85], [94, 63], [98, 68], [50, 69], [44, 29], [61, 39], [97, 74]],
    [[84, 45], [81, 82], [74, 21], [86, 54], [32, 61], [43, 35], [81, 18], [82, 87], [12, 77], [65, 62], [91, 38], [64, 37], [19, 43], [82, 87], [96, 34], [98, 87], [51, 87], [14, 30], [81, 85], [64, 75], [88, 94], [89, 19], [58, 92], [53, 30], [57, 95], [67, 28], [79, 39], [94, 87], [97, 67], [72, 29], [23, 87], [19, 69], [19, 46], [96, 91], [84, 37], [33, 46], [64, 77], [84, 55], [99, 52], [100, 95], [57, 12], [32, 49], [64, 74], [27, 20], [82, 70], [48, 87], [72, 89], [52, 95], [
     84, 63], [57, 91], [88, 80], [90, 29], [90, 11], [13, 94], [12, 13], [17, 44], [94, 38], [69, 23], [81, 63], [58, 87], [89, 12], [38, 55], [59, 38], [61, 17], [32, 73], [16, 39], [16, 79], [80, 98], [72, 17], [40, 32], [63, 55], [99, 77], [51, 19], [51, 76], [58, 76], [25, 51], [65, 98], [61, 30], [74, 70], [56, 39], [57, 54], [19, 15], [76, 77], [24, 29], [49, 78], [99, 92], [26, 75], [94, 71], [83, 22], [91, 44], [25, 12], [84, 69], [64, 100], [40, 57], [16, 27], [72, 98]],
    [[82, 12], [35, 54], [64, 46], [40, 59], [72, 89], [26, 34], [27, 100], [58, 30], [41, 31], [33, 18], [15, 63], [59, 68], [
     13, 39], [67, 13], [48, 75], [44, 71], [59, 46], [12, 37], [35, 76], [78, 15], [40, 10], [78, 86], [84, 87], [31, 71]],
    [[80, 47], [69, 46], [27, 61], [36, 85], [78, 95], [97, 53], [89, 95], [32, 17], [19, 31], [41, 19], [51, 44], [18, 71], [84, 21], [35, 46], [49, 53], [62, 22], [48, 52], [51, 28], [88, 43], [42, 62], [65, 79], [98, 44], [57, 68], [26, 14], [83, 92], [23, 95], [
        57, 37], [69, 14], [59, 55], [76, 22], [98, 86], [15, 23], [96, 78], [71, 95], [54, 95], [72, 87], [26, 37], [51, 38], [17, 13], [83, 78], [48, 40], [17, 68], [89, 91], [32, 39], [85, 22], [96, 90], [11, 28], [22, 95], [67, 37], [89, 61], [43, 84], [58, 91], [19, 93]],
    [[18, 23], [17, 86], [11, 93], [81, 74], [17, 28], [33, 35], [34, 67], [
     65, 35], [98, 86], [48, 100], [18, 23], [50, 82], [89, 33], [91, 63]],
    [[35, 13], [96, 11], [64, 78], [40, 14], [56, 49], [40, 50], [86, 14], [88, 49], [74, 92], [76, 77], [82, 76], [11, 15], [26, 22], [66, 37], [
     10, 31], [59, 11], [60, 31], [26, 98], [16, 67], [35, 39], [62, 39], [17, 29], [82, 42], [23, 55], [10, 98], [72, 27], [74, 11], [45, 23]],
    [[82, 67], [83, 87], [50, 39], [81, 30], [32, 90], [83, 45], [46, 94], [41, 53], [98, 99], [41, 34], [27, 36], [60, 69], [90, 52], [89, 19], [88, 83], [24, 16], [83, 55], [51, 21], [42, 20], [
        32, 57], [19, 71], [49, 18], [54, 95], [67, 44], [18, 39], [21, 71], [13, 53], [33, 78], [13, 87], [70, 55], [64, 19], [56, 73], [28, 45], [61, 23], [89, 87], [98, 93], [67, 28], [56, 36], [52, 36]],
    [[92, 62], [89, 85], [84, 54], [83, 45], [41, 45], [25, 62], [10, 76], [89, 75], [78, 63], [32, 21], [81, 17], [72, 86], [42, 21], [49, 53], [64, 72], [11, 76], [21, 53], [56, 29], [65, 25], [49, 34], [34, 36], [72, 13], [35, 15], [70, 62], [
        57, 29], [41, 57], [38, 86], [65, 36], [35, 45], [64, 15], [89, 90], [89, 86], [65, 42], [89, 61], [33, 93], [92, 23], [21, 63], [36, 63], [10, 42], [66, 38], [100, 63], [49, 99], [26, 21], [33, 25], [72, 71], [72, 94], [49, 98], [24, 90], [78, 95]],
    [[32, 97], [10, 76], [66, 19], [44, 54], [97, 37], [10, 61], [27, 62], [65, 44], [48, 11], [91, 68], [10, 34], [33, 55], [64, 14], [74, 76], [24, 70], [84, 39], [29, 47], [12, 54], [56, 92], [50, 68], [98, 43], [44, 85], [50, 91], [19, 28], [26, 35], [100, 54], [77, 47], [33, 76], [97, 14], [26, 92], [81, 55], [89, 89], [64, 77], [28, 13], [72, 59], [60, 78], [64, 55], [56, 17], [96, 60], [96, 91], [59, 21], [77, 61], [81, 34], [85, 78], [33, 59], [94, 71], [30, 63], [33, 54], [26, 95], [88, 67], [90, 67], [57, 71], [90, 69], [67, 12], [72, 13], [90, 23], [83, 28], [34, 60], [56, 65], [80, 61], [45, 95], [17, 55], [11, 84], [60, 38], [43, 93], [58, 27], [27, 39], [94, 71], [72, 14], [29, 30], [53, 54], [56, 77], [80, 85], [74, 60], [74, 37], [66, 11], [76, 95], [36, 22], [32, 67], [56, 98], [32, 67], [72, 85], [35, 13], [65, 10], [92, 94], [80, 92]], ]
dataset_7 = [
    [[57, 14], [75, 62], [32, 22], [42, 38], [27, 100], [96, 74], [73, 19], [17, 95], [98, 53], [36, 77], [76, 87], [51, 55], [64, 41], [67, 95], [10, 85], [54, 31], [94, 47], [73, 18], [69, 79], [36, 68], [41, 61], [10, 99], [56, 27], [97, 26], [64, 43], [11, 79], [85, 54], [81, 25], [88, 69], [
     41, 13], [87, 55], [44, 94], [56, 58], [49, 75], [32, 39], [34, 82], [72, 52], [77, 30], [41, 74], [69, 78], [90, 43], [16, 90], [25, 82], [64, 92], [66, 61], [67, 28], [91, 13], [19, 84], [26, 94], [18, 23], [73, 44], [25, 27], [83, 36], [73, 98], [97, 92], [43, 52], [21, 85], [98, 87]],
    [[41, 69], [20, 70], [84, 55], [82, 75], [65, 11], [96, 54], [10, 79], [60, 30], [64, 15], [64, 95], [
     80, 90], [59, 36], [48, 33], [41, 85], [94, 63], [98, 68], [50, 69], [44, 29], [61, 39], [97, 74]],
    [[84, 45], [81, 82], [74, 21], [86, 54], [32, 61], [43, 35], [81, 18], [82, 87], [12, 77], [65, 62], [91, 38], [64, 37], [19, 43], [82, 87], [96, 34], [98, 87], [51, 87], [14, 30], [81, 85], [64, 75], [88, 94], [89, 19], [58, 92], [53, 30], [57, 95], [67, 28], [79, 39], [94, 87], [97, 67], [72, 29], [23, 87], [19, 69], [19, 46], [96, 91], [84, 37], [33, 46], [64, 77], [84, 55], [99, 52], [100, 95], [57, 12], [32, 49], [64, 74], [27, 20], [82, 70], [48, 87], [72, 89], [52, 95], [
     84, 63], [57, 91], [88, 80], [90, 29], [90, 11], [13, 94], [12, 13], [17, 44], [94, 38], [69, 23], [81, 63], [58, 87], [89, 12], [38, 55], [59, 38], [61, 17], [32, 73], [16, 39], [16, 79], [80, 98], [72, 17], [40, 32], [63, 55], [99, 77], [51, 19], [51, 76], [58, 76], [25, 51], [65, 98], [61, 30], [74, 70], [56, 39], [57, 54], [19, 15], [76, 77], [24, 29], [49, 78], [99, 92], [26, 75], [94, 71], [83, 22], [91, 44], [25, 12], [84, 69], [64, 100], [40, 57], [16, 27], [72, 98]],
    [[82, 12], [35, 54], [64, 46], [40, 59], [72, 89], [26, 34], [27, 100], [58, 30], [41, 31], [33, 18], [15, 63], [59, 68], [
     13, 39], [67, 13], [48, 75], [44, 71], [59, 46], [12, 37], [35, 76], [78, 15], [40, 10], [78, 86], [84, 87], [31, 71]],
    [[80, 47], [69, 46], [27, 61], [36, 85], [78, 95], [97, 53], [89, 95], [32, 17], [19, 31], [41, 19], [51, 44], [18, 71], [84, 21], [35, 46], [49, 53], [62, 22], [48, 52], [51, 28], [88, 43], [42, 62], [65, 79], [98, 44], [57, 68], [26, 14], [83, 92], [23, 95], [
     57, 37], [69, 14], [59, 55], [76, 22], [98, 86], [15, 23], [96, 78], [71, 95], [54, 95], [72, 87], [26, 37], [51, 38], [17, 13], [83, 78], [48, 40], [17, 68], [89, 91], [32, 39], [85, 22], [96, 90], [11, 28], [22, 95], [67, 37], [89, 61], [43, 84], [58, 91], [19, 93]],
    [[18, 23], [17, 86], [11, 93], [81, 74], [17, 28], [33, 35], [34, 67], [
     65, 35], [98, 86], [48, 100], [18, 23], [50, 82], [89, 33], [91, 63]],
    [[35, 13], [96, 11], [64, 78], [40, 14], [56, 49], [40, 50], [86, 14], [88, 49], [74, 92], [76, 77], [82, 76], [11, 15], [26, 22], [66, 37], [
     10, 31], [59, 11], [60, 31], [26, 98], [16, 67], [35, 39], [62, 39], [17, 29], [82, 42], [23, 55], [10, 98], [72, 27], [74, 11], [45, 23]],
    [[82, 67], [83, 87], [50, 39], [81, 30], [32, 90], [83, 45], [46, 94], [41, 53], [98, 99], [41, 34], [27, 36], [60, 69], [90, 52], [89, 19], [88, 83], [24, 16], [83, 55], [51, 21], [42, 20], [
     32, 57], [19, 71], [49, 18], [54, 95], [67, 44], [18, 39], [21, 71], [13, 53], [33, 78], [13, 87], [70, 55], [64, 19], [56, 73], [28, 45], [61, 23], [89, 87], [98, 93], [67, 28], [56, 36], [52, 36]],
    [[92, 62], [89, 85], [84, 54], [83, 45], [41, 45], [25, 62], [10, 76], [89, 75], [78, 63], [32, 21], [81, 17], [72, 86], [42, 21], [49, 53], [64, 72], [11, 76], [21, 53], [56, 29], [65, 25], [49, 34], [34, 36], [72, 13], [35, 15], [70, 62], [
     57, 29], [41, 57], [38, 86], [65, 36], [35, 45], [64, 15], [89, 90], [89, 86], [65, 42], [89, 61], [33, 93], [92, 23], [21, 63], [36, 63], [10, 42], [66, 38], [100, 63], [49, 99], [26, 21], [33, 25], [72, 71], [72, 94], [49, 98], [24, 90], [78, 95]],
    [[32, 97], [10, 76], [66, 19], [44, 54], [97, 37], [10, 61], [27, 62], [65, 44], [48, 11], [91, 68], [10, 34], [33, 55], [64, 14], [74, 76], [24, 70], [84, 39], [29, 47], [12, 54], [56, 92], [50, 68], [98, 43], [44, 85], [50, 91], [19, 28], [26, 35], [100, 54], [77, 47], [33, 76], [97, 14], [26, 92], [81, 55], [89, 89], [64, 77], [28, 13], [72, 59], [60, 78], [64, 55], [56, 17], [96, 60], [96, 91], [59, 21], [77, 61], [81, 34], [
     85, 78], [33, 59], [94, 71], [30, 63], [33, 54], [26, 95], [88, 67], [90, 67], [57, 71], [90, 69], [67, 12], [72, 13], [90, 23], [83, 28], [34, 60], [56, 65], [80, 61], [45, 95], [17, 55], [11, 84], [60, 38], [43, 93], [58, 27], [27, 39], [94, 71], [72, 14], [29, 30], [53, 54], [56, 77], [80, 85], [74, 60], [74, 37], [66, 11], [76, 95], [36, 22], [32, 67], [56, 98], [32, 67], [72, 85], [35, 13], [65, 10], [92, 94], [80, 92]],
]
dataset_8 = [
    [25, 84, 83, 71, 59, 82, 70, 67, 41, 14, 53, 80, 99, 84, 81, 47, 92, 90, 83, 82, 21, 100, 100, 69, 26, 27, 97, 32, 89, 13, 0, 71, 88, 50, 42, 15, 16, 64, 28, 19, 91, 59, 0, 15, 88, 23, 52, 2,
     99, 17, 52, 40, 60, 84, 18, 7, 0, 65, 27, 62, 7, 32, 66, 45, 28, 19, 21, 66, 12, 37, 71, 100, 92, 18, 83, 15, 5, 89, 75, 36, 41, 40, 68, 30, 32, 0, 54, 90, 68, 38, 0, 81, 58, 94, 57, 35, 49],
    [44, 64, 61, 2, 29, 1, 50, 75, 47, 54, 46, 95, 57, 55, 35, 3, 97, 74, 81, 35, 36, 56, 76, 54, 37, 94, 4, 32, 19, 88, 9, 87, 53, 27, 100, 64, 13, 84, 15, 16, 25, 50, 95, 5, 10, 43, 42, 9, 10,
     20, 9, 87, 84, 5, 36, 32, 50, 41, 98, 2, 13, 48, 46, 55, 79, 83, 81, 60, 50, 21, 81, 30, 3, 8, 99, 10, 85, 10, 25, 86, 58, 27, 25, 33, 62, 1, 60, 16, 82, 12, 74, 90, 1, 5, 91, 23, 76, 53],
    [76, 23, 43, 46, 90, 22, 20, 15, 34, 27, 31, 98, 25, 50, 80, 70, 8, 78, 36, 100, 70, 89, 70, 21, 33, 62, 9, 57, 79, 62, 77, 61, 39, 69, 81, 34, 40, 33, 20, 45, 77, 40, 81, 80, 17, 52, 93, 93, 58, 45,
     33, 87, 9, 44, 67, 72, 52, 11, 16, 54, 52, 97, 5, 18, 39, 18, 48, 26, 89, 21, 74, 58, 77, 51, 35, 100, 32, 72, 80, 46, 76, 45, 96, 47, 73, 57, 56, 96, 86, 3, 22, 7, 25, 27, 45, 95, 80, 79, 39, 29],
    [99, 56, 2, 23, 51, 95, 92, 73, 37, 43, 99, 21, 51, 73, 23, 17, 22, 73, 95, 18, 80, 97, 92, 99, 34, 100, 72, 12, 92, 15, 46, 51, 3, 62, 2, 57, 45, 79, 90, 51, 95, 4, 48, 17, 39, 93,
        31, 73, 100, 6, 44, 72, 45, 3, 30, 14, 53, 31, 62, 70, 38, 92, 83, 40, 0, 77, 14, 97, 34, 93, 41, 46, 39, 6, 39, 18, 49, 38, 48, 67, 66, 34, 42, 82, 64, 32, 2, 34, 27, 68, 55],
    [47, 27, 37, 1, 39, 42, 57, 66, 37, 17, 15, 48, 94, 96, 24, 25, 65, 55, 73, 35, 31, 13, 21, 69, 60, 24, 72, 3, 67, 71, 57, 42, 79, 8, 84, 19, 64, 60, 22, 5, 75, 100, 70, 68, 17, 92,
        97, 77, 21, 25, 37, 56, 56, 37, 32, 14, 40, 53, 10, 8, 84, 37, 79, 69, 48, 28, 14, 22, 89, 59, 44, 8, 73, 82, 93, 73, 0, 21, 66, 24, 13, 28, 38, 84, 53, 88, 14, 9, 96, 58, 96],
    [35, 16, 47, 14, 90, 53, 31, 70, 95, 63, 33, 86, 44, 56, 5, 14, 58, 55, 9, 89, 2, 28, 67, 88, 100, 59, 24, 78, 80, 33, 30, 73, 64, 13, 82, 69, 26, 79, 68, 8, 65, 44, 62, 81, 19,
     41, 19, 20, 9, 2, 96, 78, 17, 88, 65, 85, 84, 30, 72, 20, 82, 25, 62, 74, 61, 88, 46, 33, 43, 78, 83, 74, 20, 39, 7, 26, 30, 24, 39, 96, 100, 62, 12, 35, 98, 22, 86, 62, 99, 35],
    [7, 50, 60, 0, 0, 88, 30, 80, 27, 73, 14, 83, 36, 80, 59, 99, 26, 25, 15, 87, 27, 9, 48, 8, 63, 78, 77, 24, 90, 61, 49, 5, 29, 72, 31, 68, 41, 19, 8, 29, 98, 63, 12, 37, 7, 1, 22, 25, 36,
     22, 85, 5, 64, 96, 89, 40, 3, 56, 65, 70, 18, 92, 86, 27, 94, 82, 61, 100, 91, 61, 47, 63, 84, 62, 53, 5, 2, 19, 34, 60, 35, 3, 29, 52, 64, 39, 4, 55, 59, 49, 95, 40, 45, 95, 17, 92, 25, 20],
    [28, 60, 51, 97, 6, 79, 3, 73, 97, 81, 88, 21, 78, 39, 97, 69, 35, 90, 90, 56, 6, 31, 83, 54, 65, 96, 92, 20, 94, 35, 18, 67, 31, 57, 76, 10, 8, 40, 100, 98, 4, 69, 75, 14, 75, 73, 53, 36,
     15, 33, 63, 30, 27, 59, 75, 54, 97, 9, 73, 15, 30, 9, 17, 32, 70, 93, 81, 82, 6, 44, 56, 75, 73, 17, 88, 3, 36, 99, 63, 62, 16, 14, 81, 67, 33, 48, 11, 50, 92, 34, 46, 54, 36, 90, 76, 44],
    [16, 20, 70, 37, 16, 15, 20, 92, 44, 79, 49, 62, 3, 83, 84, 29, 11, 34, 81, 58, 22, 57, 38, 21, 12, 99, 17, 49, 36, 89, 43, 51, 60, 88, 69, 0, 17, 46, 35, 88, 93, 6, 29, 63, 97, 44, 37,
     67, 86, 38, 88, 9, 78, 9, 57, 91, 60, 41, 36, 81, 88, 3, 2, 22, 79, 82, 81, 82, 32, 95, 72, 94, 79, 19, 1, 5, 59, 100, 40, 5, 1, 12, 41, 83, 27, 49, 19, 53, 11, 75, 61, 85, 37, 62],
    [30, 30, 46, 91, 61, 28, 18, 7, 46, 53, 85, 79, 87, 53, 58, 25, 8, 100, 55, 55, 24, 23, 56, 99, 68, 43, 20, 71, 71, 0, 2, 74, 71, 73, 99, 22, 96, 85, 78, 93, 0, 21, 65, 38, 5, 82, 99, 92,
     60, 75, 97, 22, 67, 60, 100, 0, 48, 79, 77, 66, 35, 86, 93, 8, 19, 49, 62, 51, 57, 26, 98, 42, 68, 66, 2, 7, 80, 75, 94, 80, 90, 85, 60, 44, 55, 44, 63, 13, 100, 64, 71, 47, 6, 20, 15, 25],
]
dataset_9 = [
    ['jvvp', 'fdjtp', 'pgzk', 'but', 'm', 'pnuv', 'gp', 'osn', 'r', 'l', 'kao', 'ggxd', 'tnn', 'vudf', 'btrn', 'hkk', 'ilx', 'osg', 'nars', 'igl', 'sgg', 'mds', 'ckg', 'uj',
     'pn', 'frgadh', 'muqg', 'xvhzf', 'dhib', 'hccu', 'melqw', 'rpox', 'xqpq', 'dxqel', 'zebga', 'qicn', 'ptkn', 's', 'vbvt', 'zuv', 'kql', 'el', 'xdn', 'chso', 'ztwz', 'ndkt'],
    ['end', 'wc', 'fjvs', 'pvr', 'yv', 'yeus', 'bob', 'jhoi', 'ofoq', 'wwwkma', 'ghlhylg', 'hjcne', 'zfknf', 'iywilb', 'pezooov', 'nvxilax', 'jryik', 'podg', 'hwmf',
     'msxs', 'aayr', 'dxen', 'bzsmh', 'pqlik', 'cavuam', 'fxupnc', 'vmtthy', 'hwmqn', 'xfi', 'mvelli', 'qdr', 'rht', 'wde', 'otkmkp', 'xaxtci', 'iyrd', 'vbxpff', 'k'],
    ['uku', 'bxh', 'yri', 'sm', 'yuo', 'tqmu', 'zzq', 'jxd', 'onmvsk', 'dep', 'xodja', 'imijn', 'cmdt', 'krb', 'lgci', 'kwe', 'hq', 'h', 'cgyqi', 'pwdic', 'pey', 'brojr', 'bozcv', 'jciws', 'v', 'q', 'fgltd',
     'vnmriw', 'wghu', 'nsxa', 'xolqj', 'cfw', 'em', 'dm', 'y', 'u', 'x', 'aiqjrgx', 'poznjk', 'ppdymjt', 'evhk', 'nqo', 'pjspuu', 'taqg', 'npyj', 'herhzoa', 'pxche', 'hcdn', 'bce', 'ya', 'up', 'afe', 'on', 'j'],
    ['grns', 'ikeh', 'mcn', 'pot', 'jxt', 'eryp', 'yhqvtitta', 'cuvifem', 'tkubtnsth', 'yvkdti', 'un', 'smhqnxb', 'cxdtce', 'jlqeoil', 'lcpxivy', 'cznvcv', 'nzvl',
     'zajdu', 'hcljnzf', 'lmwxny', 'mkrs', 'oukwc', 'fdykcy', 'yig', 'oenkja', 'giygrwh', 'qbsout', 'ppmhqu', 'xalxo', 'tbvau', 'dptpzm', 'ovwor', 'bext'],
    ['c', 'zh', 'xnm', 'wjad', 'rtes', 'oppn', 'ayd', 'hhs', 'fx', 'epw', 'moi', 'bue', 'tza', 'azz', 'nid',
     'vyly', 'ice', 'elk', 'fzqj', 'fgz', 'tpt', 'nwd', 'guk', 'ywas', 'war', 'xkt', 'det', 'zqe', 'ew', 'ai'],
    ['fzjc', 'iik', 'wad', 'bks', 'nkaj', 'ukiv', 'wzdl', 'cqnd', 'bws', 'qil', 'nuj', 'jjpjg', 'fgbe', 'fxoxfj', 'gxf', 'tex', 'kwnh', 'vvqt', 'ugcb',
     'ndmb', 'gxe', 'pngq', 'eahp', 'gcow', 'kkc', 'wkb', 'mmmx', 'cigq', 'zygn', 'dblj', 'ikim', 'pscdu', 'rckii', 'yfy', 'xc', 'd', 'ylfnuijn'],
    ['ec', 'std', 'vs', 'uyiq', 'ejr', 'oau', 'fxll', 'tvth', 'nmi', 'vdhz', 'fege', 'hxdolh', 'fpobs', 'tsbgp', 'wkcne', 'dqeo', 'hgcyvn', 'oof', 'pqx', 'in',
     'izdb', 'cuv', 'ndb', 'iakm', 'tks', 'uuwq', 'pji', 'meyw', 'ejlkm', 'zph', 'cbryl', 'irn', 'rll', 'arti', 'juy', 'ea', 'pj', 'ar', 'xb', 'vy', 'kao'],
    ['yqve', 'aurq', 'rs', 'fa', 'jbra', 'nmk', 'vwhe', 'qtd', 'gzjll', 'ral', 'uwb', 'huz', 'jfq', 'emm', 'pvb', 'tmza', 'lhp', 'anss', 'bmhg', 'maqan',
     'qqh', 'xcf', 'sedha', 'sdq', 'hoo', 'rrdd', 'opo', 'yxc', 'pce', 'gsvn', 'eae', 'qjae', 'jkh', 'krc', 'cyx', 'auoy', 'fxp', 'wt', 'l', 'be'],
    ['sm', 'dmd', 'to', 'qkw', 'qgz', 'zgmf', 'sqvpd', 'wjbz', 'kzfz', 'ezq', 'bpch', 'afit', 'ilva', 'sru', 'trsr', 'gem', 'rwe', 'nzt', 'xfj', 'as', 'mz', 'g', 'or', 'in', 'og', 'xq', 'js', 'm', 'lhzf', 'amn',
     'ieukp', 'kwwc', 'ztyd', 'yyjw', 'prci', 'pcqo', 'zaxv', 'bkz', 'ate', 'dh', 'xwfy', 'yhmi', 'ruh', 'lh', 'iq', 'wcms', 'lax', 'dff', 'ldzu', 'xzjs', 'yo', 'xk', 'nd', 'wxx', 'j', 'ux', 'vcg', 'zi', 'me'],
    ['rng', 'aid', 'mmd', 'jzam', 'sghi', 'hukk', 'uuwe', 'jdzg', 'uxdlaw', 'tllk', 'gjmb', 'uujxd', 'opjoubo', 'mn', 'lsnpi', 'xqg', 'hts', 'puuj', 'pdy', 'vkas', 'rkfs', 'lhlz', 'ryo',
     'ejx', 'gg', 'ffx', 'iqfj', 'mdxs', 'spcb', 'gnsaw', 'tatt', 'pev', 'ozsl', 'jev', 'r', 'hgjk', 'ohj', 'dlfec', 'hzaw', 'wm', 'opfw', 'aktf', 'if', 'bnyk', 'p', 'fc', 'b', 'r', 'l'],
]


def handleAlgorithmWithDataset(algorithm: int,
                               dataset: int):
    total_time_taken: list = []
    chosen_dataset: list = []
    final_output: list = []
    result_list: list = []
    input_array: list = []
    csvData: list = []
    w: list = []
    v: list = []
    X: str = ''
    Y: str = ''

    if (dataset == 0):
        chosen_dataset = dataset_0
    elif (dataset == 1):
        chosen_dataset = dataset_1
    elif (dataset == 2):
        chosen_dataset = dataset_2
    elif (dataset == 3):
        chosen_dataset = dataset_3
    elif (dataset == 4):
        chosen_dataset = dataset_4
    elif (dataset == 5):
        chosen_dataset = dataset_5
    elif (dataset == 6):
        chosen_dataset = dataset_6
    elif (dataset == 7):
        chosen_dataset = dataset_7
    elif (dataset == 8):
        chosen_dataset = dataset_8
    elif (dataset == 9):
        chosen_dataset = dataset_9

    if algorithm == 8:
        # COIN CHANGE MAKING

        for row in chosen_dataset:
            start = time.time()
            result_list.append(countSelection(input_array))
            end = time.time()
            total_time_taken.append(end - start)


    elif algorithm == 5:
        # KNAPSACK

        for row in chosen_dataset:
            w, v = [], []
            for item in row:
                w.append(item[0])
                v.append(item[1])
            start = time.time()
            result_list.append(knapsackSelection(w, v))
            end = time.time()
            total_time_taken.append(end - start)

    elif algorithm == 2:
        # LEVENSHTEIN DISTANCE

        for row in chosen_dataset:
            start = time.time()
            result_list.append(levenshteinDynamic(row[0], row[1]))
            end = time.time()
            total_time_taken.append(end - start)

    elif algorithm == 3:
        # LONGEST COMMON SUBSEQUENCE

        for row in chosen_dataset:
            start = time.time()
            result_list.append(longestIncreasingSubsequence(row, len(row)))
            end = time.time()
            total_time_taken.append(end -start)

    elif algorithm == 0:
        # LONGEST INCREASING SUBSEQUENCE

        for row in chosen_dataset:
            start = time.time()
            result_list.append(longestCommonSubsequenceSelection(row[0], row[1]))
            end = time.time()
            total_time_taken.append(end - start)

    elif algorithm == 4:
        # MATRIX CHAIN MULTIPLICATION

        for row in chosen_dataset:
            start = time.time()
            result_list.append(matrixChainOrderSelection(row))
            end = time.time()
            total_time_taken.append(end - start)

    elif algorithm == 6:
        # PARTITION

        for row in chosen_dataset: 
            v = []
            for item in row:
                v.append(int(item[1]))
            start = time.time()
            result_list.append(findPartitionDynamicProgramming(v, len(v)))
            end = time.time()
            total_time_taken.append(end - start)

    elif algorithm == 7:
        # ROD CUTTING

        for row in chosen_dataset: 
            v = []
            for item in row:
                v.append(int(item[1]))
            start = time.time()
            result_list.append(findPartitionDynamicProgramming(v, len(v)))   
            end = time.time()
            total_time_taken.append(end - start)     

    elif algorithm == 1:
        # SHORTEST COMMON SUPERSEQUENCE

        for row in chosen_dataset:
            start = time.time()
            result_list.append(superSeqSelection(row[0], row[1]))
            end = time.time()
            total_time_taken.append(end - start)

    elif algorithm == 9:
        # WORD BREAK

        for row in chosen_dataset:
            final_output = []
            start = time.time()
            wordBreak(row, 'Saif', final_output)
            end = time.time()
            total_time_taken.append(end - start)
            result_list.append(final_output)

    return result_list, total_time_taken
