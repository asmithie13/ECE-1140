import CTC
from CTC import TempData

class Line_Dictionary():

    ##start
    green = [
        ['K_63', 70, False, 'N/A', 'N/A'],
        ['K_64', 70, False, 'Approching GLENBURY', 'N/A'],
        ['K_65', 70, False, 'Welcome to GLENBURY', '1'],
        ['K_66', 70, False, 'N/A', 'N/A'],
        ['K_67', 40, False, 'N/A', 'N/A'],
        ['K_68', 40, False, 'N/A', 'N/A'],
        ['L_69', 40, False, 'N/A', 'N/A'],
        ['L_70', 40, False, 'N/A', 'N/A'],
        ['L_71', 40, False, 'N/A', 'N/A'],
        ['L_72', 40, False, 'Approching DORMONT', 'N/A'],
        ['L_73', 40, False, 'Welcome to DORMONT', '1'],
        ['M_74', 40, False, 'N/A', 'N/A'],
        ['M_75', 40, False, 'N/A', 'N/A'],
        ['M_76', 40, False, 'APPROACHING MT LEBANON', 'N/A'],
        ['N_77', 70, False, 'Welcome to MT LEBANON', '1'],
        ['N_78', 70, False, 'N/A', 'N/A'],
        ['N_79', 70, False, 'N/A', 'N/A'],
        ['N_80', 70, False, 'N/A', 'N/A'],
        ['N_81', 70, False, 'N/A', 'N/A'],
        ['N_82', 70, False, 'N/A', 'N/A'],
        ['N_83', 70, False, 'N/A', 'N/A'],
        ['N_84', 70, False, 'N/A', 'N/A'],
        ['N_85', 70, False, 'N/A', 'N/A'],
        ['O_86', 25, False, 'N/A', 'N/A'],
        ['O_87', 25, False, 'Approching POPLAR', 'N/A'],
        ['O_88', 25, False, 'Welcome to POPLAR', '2'],
        ['P_89', 25, False, 'N/A', 'N/A'],
        ['P_90', 25, False, 'N/A', 'N/A'],
        ['P_91', 25, False, 'N/A', 'N/A'],
        ['P_92', 25, False, 'N/A', 'N/A'],
        ['P_93', 25, False, 'N/A', 'N/A'],
        ['P_94', 25, False, 'N/A', 'N/A'],
        ['P_95', 25, False, 'Approching CASTLE SHANNON', 'N/A'],
        ['P_96', 25, False, 'Welcome to CASTLE SHANNON', '2'],
        ['P_97', 25, False, 'N/A', 'N/A'],
        ['Q_98', 25, False, 'N/A', 'N/A'],
        ['Q_99', 25, False, 'N/A', 'N/A'],
        ['Q_100', 25, False, 'N/A', 'N/A'],	#change dir
        ['N_85', 70, False, 'N/A', 'N/A'],
        ['N_84', 70, False, 'N/A', 'N/A'],
        ['N_83', 70, False, 'N/A', 'N/A'],
        ['N_82', 70, False, 'N/A', 'N/A'],
        ['N_81', 70, False, 'N/A', 'N/A'],
        ['N_80', 70, False, 'N/A', 'N/A'],
        ['N_79', 70, False, 'N/A', 'N/A'],
        ['N_78', 70, False, 'Approching MT LEBANON', 'N/A'],
        ['N_77', 70, False, 'Welcome to MT LEBANON', '2'],
        ['R_101', 26, False, 'N/A', 'N/A'], #new section
        ['S_102', 28, False, 'N/A', 'N/A'],
        ['S_103', 28, False, 'N/A', 'N/A'],
        ['S_104', 28, False, 'Approching DORMONT', 'N/A'],
        ['T_105', 28, False, 'Welcome to DORMONT', '1'],
        ['T_106', 28, False, 'N/A', 'N/A'],
        ['T_107', 28, False, 'N/A', 'N/A'],
        ['T_108', 28, False, 'N/A', 'N/A'],
        ['T_109', 28, False, 'N/A', 'N/A'],
        ['U_110', 30, False, 'N/A', 'N/A'],
        ['U_111', 30, False, 'N/A', 'N/A'],
        ['U_112', 30, False, 'N/A', 'N/A'],
        ['U_113', 30, False, 'Approaching GLENBURY', 'N/A'],
        ['U_114', 30, False, 'Welcome to GLENBURY', '1'],
        ['U_115', 30, False, 'N/A', 'N/A'],
        ['U_116', 30, False, 'N/A', 'N/A'],
        ['V_117', 15, False, 'N/A', 'N/A'],
        ['V_118', 15, False, 'N/A', 'N/A'],
        ['V_119', 15, False, 'N/A', 'N/A'],
        ['V_120', 15, False, 'N/A', 'N/A'],
        ['V_121', 15, False, 'N/A', 'N/A'],
        ['W_122', 20, True, 'Approaching OVERBROOK', 'N/A'],
        ['W_123', 20, True, 'Welcome to OVERBROOK', '1'],
        ['W_124', 20, True, 'N/A', 'N/A'],
        ['W_125', 20, True, 'N/A', 'N/A'],
        ['W_126', 20, True, 'N/A', 'N/A'],
        ['W_127', 20, True, 'N/A', 'N/A'],
        ['W_128', 20, True, 'N/A', 'N/A'],
        ['W_129', 20, True, 'N/A', 'N/A'],
        ['W_130', 20, True, 'N/A', 'N/A'],
        ['W_131', 20, True, 'Apporaching INGLEWOOD', 'N/A'],
        ['W_132', 20, True, 'Welcome to INGLEWOOD', '2'],
        ['W_133', 20, True, 'N/A', 'N/A'],
        ['W_134', 20, True, 'N/A', 'N/A'],
        ['W_135', 20, True, 'N/A', 'N/A'],
        ['W_136', 20, True, 'N/A', 'N/A'],
        ['W_137', 20, True, 'N/A', 'N/A'],
        ['W_138', 20, True, 'N/A', 'N/A'],
        ['W_139', 20, True, 'N/A', 'N/A'],
        ['W_140', 20, True, 'Approaching CENTRAL', 'N/A'],
        ['W_141', 20, True, 'Welcome to CENTRAL', '1'],
        ['W_142', 20, True, 'N/A', 'N/A'],
        ['W_143', 20, True, 'N/A', 'N/A'],
        ['X_144', 20, False, 'N/A', 'N/A'],
        ['X_145', 20, False, 'N/A', 'N/A'],
        ['X_146', 20, False, 'N/A', 'N/A'],
        ['Y_147', 20, False, 'N/A', 'N/A'],
        ['Y_148', 20, False, 'N/A', 'N/A'],
        ['Y_149', 20, False, 'N/A', 'N/A'],
        ['Z_150', 20, False, 'N/A', 'N/A'],
        ['F_28', 30, False, 'N/A', 'N/A'],
        ['F_27', 30, False, 'N/A', 'N/A'],
        ['F_26', 70, False, 'N/A', 'N/A'],
        ['F_25', 70, False, 'N/A', 'N/A'],
        ['F_24', 70, False, 'N/A', 'N/A'],
        ['F_23', 70, False, 'Apporaching WHITED', 'N/A'],
        ['F_22', 70, False, 'Welcome to WHITED', '1'],
        ['F_21', 70, False, 'N/A', 'N/A'],
        ['E_20', 60, False, 'N/A', 'N/A'],
        ['E_19', 60, False, 'N/A', 'N/A'],
        ['E_18', 60, False, 'N/A', 'N/A'],
        ['E_17', 60, False, 'Approaching STATION', 'N/A'],
        ['D_16', 70, False, 'Welcome to Station', '1'], 
        ['D_15', 70, False, 'N/A', 'N/A'],
        ['D_14', 70, False, 'N/A', 'N/A'],
        ['D_13', 70, False, 'N/A', 'N/A'],
        ['C_12', 45, False, 'N/A', 'N/A'],
        ['C_11', 45, False, 'N/A', 'N/A'],
        ['C_10', 45, False, 'Apporaching EDGEBROOK', 'N/A'],
        ['C_9', 45, False, 'Welcome to EDGEBROOK', '2'],
        ['C_8', 45, False, 'N/A', 'N/A'],
        ['C_7', 45, False, 'N/A', 'N/A'],
        ['B_6', 45, False, 'N/A', 'N/A'],
        ['B_5', 45, False, 'N/A', 'N/A'],
        ['B_4', 45, False, 'N/A', 'N/A'],
        ['A_3', 45, False, 'Approching PIONEER', 'N/A'],
        ['A_2', 45, False, 'PIONEER', '2'],
        ['A_1', 45, False, 'N/A', 'N/A'],
        ['D_13', 70, False, 'N/A', 'N/A'], #new section
        ['D_14', 70, False, 'N/A', 'N/A'],
        ['D_15', 70, False, 'Apporaching STATION', 'N/A'],
        ['D_16', 70, False, 'Welcome to STATION', '2'],
        ['E_17', 60, False, 'N/A', 'N/A'],
        ['E_18', 60, False, 'N/A', 'N/A'],
        ['E_19', 60, False, 'N/A', 'N/A'],
        ['E_20', 60, False, 'N/A', 'N/A'],
        ['F_21', 70, False, 'Apporaching WHITED', 'N/A'],
        ['F_22', 70, False, 'Welcome to WHITED', '2'],
        ['F_23', 70, False, 'N/A', 'N/A'],
        ['F_24', 70, False, 'N/A', 'N/A'],
        ['F_25', 70, False, 'N/A', 'N/A'],
        ['F_26', 70, False, 'N/A', 'N/A'],
        ['F_27', 30, False, 'N/A', 'N/A'],
        ['F_28', 30, False, 'N/A', 'N/A'],
        ['G_29', 30, False, 'N/A', 'N/A'],
        ['G_30', 30, False, 'Apporaching SOUTH BANK', 'N/A'],
        ['G_31', 30, False, 'Welcome to SOUTH BANK', '2'],
        ['G_32', 30, False, 'N/A', 'N/A'],
        ['H_33', 30, False, 'N/A', 'N/A'],
        ['H_34', 30, False, 'N/A', 'N/A'],
        ['H_35', 30, False, 'N/A', 'N/A'],
        ['I_36', 30, True, 'N/A', 'N/A'],
        ['I_37', 30, True,'Apporachning CENTRAL', 'N/A'],
        ['I_38', 30, True,'Welcome to CENTRAL', 'N/A'],
        ['I_39', 30, True,'N/A' , '1'],
        ['I_40', 30, True, 'N/A', 'N/A'],
        ['I_41', 30, True, 'N/A', 'N/A'],
        ['I_42', 30, True, 'N/A', 'N/A'],
        ['I_43', 30, True, 'N/A', 'N/A'],
        ['I_44', 30, True, 'N/A', 'N/A'],
        ['I_45', 30, True, 'N/A', 'N/A'],
        ['I_46', 30, True, 'Apporaching INGLEWOOD', 'N/A'],
        ['I_47', 30, True,'Welcome to INGLEWOOD' , 'N/A'],
        ['I_48', 30, True,'N/A' , '1'],
        ['I_49', 30, True, 'N/A', 'N/A'],
        ['I_50', 30, True, 'N/A', 'N/A'],
        ['I_51', 30, True, 'N/A', 'N/A'],
        ['I_52', 30, True, 'N/A', 'N/A'],
        ['I_53', 30, True, 'N/A', 'N/A'],
        ['I_54', 30, True, 'N/A', 'N/A'],
        ['I_55', 30, True, 'Approaching OVERBROOK', 'N/A'],
        ['I_56', 30, True, 'Welcome to OVERBROOK', 'N/A'],
        ['I_57', 30, True, 'N/A', 'N/A'],
    ]
    
    # red = [
    #     ['D_10', 40, False, 'N/A', 'N/A'], #beacon1
    #     ['D_11', 40, False, 'N/A', 'N/A'],
    #     ['D_12', 40, False, 'N/A', 'N/A'],
    #     ['E_13', 40, False, 'N/A', 'N/A'],
    #     ['E_14', 40, False, 'N/A', 'N/A'],
    #     ['E_15', 40, False, 'Approching HERRON AVE', 'N/A'],
         
    #     ['F_16', 40, False, 'Welcome to HERRON AVE', '1'],
    #     ['F_17', 55, False, 'N/A', 'N/A'], #beacon2
    #     ['F_18', 70, False, 'N/A', 'N/A'],
    #     ['F_19', 70, False, 'N/A', 'N/A'],
    #     ['F_20', 70, False, 'Approching SWISSVILLE', 'N/A'],
    #     ['G_21', 55, False, 'Welcome to SWISSVILLE', '1'],
    #     ['G_22', 55, False, 'N/A', 'N/A'],
    #     ['G_23', 55, False, 'N/A', 'N/A'],
    #     ['H_24', 70, False, 'Approching PENN STATION', 'N/A'],
    #     ['H_25', 70, True, 'Welcome to PENN STATION', '2'],
    #     ['H_26', 70, True, 'N/A', 'N/A'],
    #     ['H_27', 70, True, 'N/A', 'N/A'],

    #     ['H_28', 70, True, 'N/A', 'N/A'], #beacon3
    #     ['H_29', 70, True, 'N/A', 'N/A'],
    #     ['H_30', 70, True, 'N/A', 'N/A'],
    #     ['H_31', 70, True, 'N/A', 'N/A'],
    #     ['H_32', 70, True, 'N/A', 'N/A'],
         
    #     ['H_33', 70, True, 'N/A', 'N/A'],
    #     ['H_34', 70, True, 'Approching STEEL PLAZA', 'N/A'], #beacon4
    #     ['H_35', 70, True, 'Welcome to STEEL PLAZA', '2'],
    #     ['H_36', 70, True, 'N/A', 'N/A'],
    #     ['H_37', 70, True, 'N/A', 'N/A'],
    #     ['H_38', 70, True, 'N/A', 'N/A'],
        
    #     ['H_39', 70, True, 'N/A', 'N/A'], #b5
    #     ['H_40', 70, True, 'N/A', 'N/A'],
    #     ['H_41', 70, True, 'N/A', 'N/A'],
    #     ['H_42', 70, True, 'N/A', 'N/A'],
    #     ['H_43', 70, True, 'N/A', 'N/A'],
    #     ['H_44', 70, True, 'Approching FIRST AVE', 'N/A'],
    #     ['H_45', 70, True, 'Welcome to FIRST AVE', '2'],
    #     ['I_46', 70, False, 'N/A', 'N/A'],
    #     ['I_47', 70, False, 'Approching STATION SQUARE', 'N/A'],
    #     ['I_48', 70, False, 'Welcome to STATION SQUARE', '2'],
    #     ['J_49', 60, False, 'N/A', 'N/A'],
    #     ['J_50', 60, False, 'N/A', 'N/A'],
    #     ['J_51', 55, False, 'N/A', 'N/A'],
    #     ['J_52', 55, False, 'N/A', 'N/A'],
        
    #     ['J_53', 55, False, 'N/A', 'N/A'], #beacon6
    #     ['J_54', 55, False, 'N/A', 'N/A'],
    #     ['K_55', 55, False, 'N/A', 'N/A'],
    #     ['K_56', 55, False, 'N/A', 'N/A'],
    #     ['K_57', 55, False, 'N/A', 'N/A'],
    #     ['L_58', 55, False, 'N/A', 'N/A'],
    #     ['L_59', 55, False, 'Approching SOUTH HILLS JUNCTION', 'N/A'],
    #     ['L_60', 55, False, 'Welcome to SOUTH HILLS JUNCTION', '2'],
    #     ['M_61', 55, False, 'N/A', 'N/A'],
    #     ['M_62', 55, False, 'N/A', 'N/A'],
    #     ['M_63', 55, False, 'N/A', 'N/A'],
    #     ['N_64', 55, False, 'N/A', 'N/A'],
    #     ['N_65', 55, False, 'N/A', 'N/A'],
    #     ['N_66', 55, False, 'N/A', 'N/A'],
        
    #     ['J_52', 55, False, 'N/A', 'N/A'],
    #     ['J_51', 55, False, 'N/A', 'N/A'], #beacon7
    #     ['J_50', 60, False, 'N/A', 'N/A'],
    #     ['J_49', 60, False, 'Approching STATION SQUARE', 'N/A'],
    #     ['I_48', 70, False, 'Welcome to STATION SQUARE', '1'],
    #     ['I_47', 70, False, 'N/A', 'N/A'],
    #     ['I_46', 70, False, 'Approching FIRST AVE', 'N/A'],
    #     ['H_45', 70, True, 'Welcome to FIRST AVE', '1'],
    #     ['H_44', 70, True, 'N/A', 'N/A'],
    #     ['H_43', 70, True, 'N/A', 'N/A'],
        
    #     ['O_67', 55, False, 'N/A', 'N/A'], #beacon8
    #     ['P_68', 55, False, 'N/A', 'N/A'],
    #     ['P_69', 55, True, 'N/A', 'N/A'],
    #     ['P_70', 55, True, 'N/A', 'N/A'],
    #     ['Q_71', 55, False, 'N/A', 'N/A'],
        
    #     ['H_38', 70, True, 'N/A', 'N/A'], #9
    #     ['H_37', 70, True, 'N/A', 'N/A'],
    #     ['H_36', 70, True, 'Approching STEEL PLAZA', 'N/A'],
    #     ['H_35', 70, True, 'Welcome to STEEL PLAZA' , '1'],
    #     ['H_34', 70, True, 'N/A', 'N/A'],
    #     ['H_33', 70, True, 'N/A', 'N/A'],
    #     ['H_32', 70, True, 'N/A', 'N/A'],
        
    #     ['R_72', 55, False, 'N/A', 'N/A'], # beacon10
    #     ['S_73', 55, False, 'N/A', 'N/A'],
    #     ['S_74', 55, True, 'N/A', 'N/A'],
    #     ['S_75', 55, True, 'N/A', 'N/A'],
    #     ['T_76', 55, False, 'N/A', 'N/A'],

    #     ['H_27', 70, True, 'N/A', 'N/A'], #beacon11
    #     ['H_26', 70, True, 'Approching PENN STATION', 'N/A'],
    #     ['H_25', 70, True, 'Welcome to PENN STATION', '1'],
    #     ['H_24', 70, False, 'N/A', 'N/A'],
    #     ['G_23', 55, False, 'N/A', 'N/A'],
    #     ['G_22', 55, False, 'Approching SWISSVILLE', 'N/A'],
    #     ['G_21', 55, False,'Welcome to SWISSVILLE', '2'],
    #     ['F_20', 70, False, 'N/A', 'N/A'],
    #     ['F_19', 70, False, 'N/A', 'N/A'],
    #     ['F_18', 70, False, 'N/A', 'N/A'],
    #     ['F_17', 55, False, 'Approching HERRON AVE', 'N/A'],
    #     ['F_16', 40, False, 'Welcome to HERRON AVE', '2'], 

    #     ['A_1', 40, False, 'N/A', 'N/A'],  #end #beacon12
    #     ['A_2', 40, False, 'N/A', 'N/A'],
    #     ['A_3', 40, False, 'N/A', 'N/A'],
    #     ['B_4', 40, False, 'N/A', 'N/A'],
    #     ['B_5', 40, False, 'N/A', 'N/A'],
    #     ['B_6', 40, False, 'Approching SHADYSIDE', 'N/A'],
    #     ['C_7', 40, False, 'Welcome to SHADYSIDE', '2'],
    #     ['C_8', 40, False, 'N/A', 'N/A'],
    #     ['C_9', 40, False, 'N/A', 'N/A']
    # ]

    b1 = [ ['D_10', 40, False, 'N/A', 'N/A'], #beacon
        ['D_11', 40, False, 'N/A', 'N/A'],
        ['D_12', 40, False, 'N/A', 'N/A'],
        ['E_13', 40, False, 'N/A', 'N/A'],
        ['E_14', 40, False, 'N/A', 'N/A'],
        ['E_15', 40, False, 'Approching HERRON AVE', 'N/A'], ]
    
    b2 = [ ['F_16', 40, False, 'Welcome to HERRON AVE', '1'],
        ['F_17', 55, False, 'N/A', 'N/A'], #beacon
        ['F_18', 70, False, 'N/A', 'N/A'],
        ['F_19', 70, False, 'N/A', 'N/A'],
        ['F_20', 70, False, 'Approching SWISSVILLE', 'N/A'],
        ['G_21', 55, False, 'Welcome to SWISSVILLE', '1'],
        ['G_22', 55, False, 'N/A', 'N/A'],
        ['G_23', 55, False, 'N/A', 'N/A'],
        ['H_24', 70, False, 'Approching PENN STATION', 'N/A'],
        ['H_25', 70, True, 'Welcome to PENN STATION', '2'],
        ['H_26', 70, True, 'N/A', 'N/A'],
        ['H_27', 70, True, 'N/A', 'N/A']
 ]
    
    b3 = [ ['H_28', 70, True, 'N/A', 'N/A'], #beacon3
        ['H_29', 70, True, 'N/A', 'N/A'],
        ['H_30', 70, True, 'N/A', 'N/A'],
        ['H_31', 70, True, 'N/A', 'N/A'],
        ['H_32', 70, True, 'N/A', 'N/A']]
    
    b4 = [ 
        ['H_33', 70, True, 'N/A', 'N/A'],
        ['H_34', 70, True, 'Approching STEEL PLAZA', 'N/A'], #beacon
        ['H_35', 70, True, 'Welcome to STEEL PLAZA', '2'],
        ['H_36', 70, True, 'N/A', 'N/A'],
        ['H_37', 70, True, 'N/A', 'N/A'],
        ['H_38', 70, True, 'N/A', 'N/A'],
    ]

    
    b5 = [ ['H_39', 70, True, 'N/A', 'N/A'], #b5
        ['H_40', 70, True, 'N/A', 'N/A'],
        ['H_41', 70, True, 'N/A', 'N/A'],
        ['H_42', 70, True, 'N/A', 'N/A'],
        ['H_43', 70, True, 'N/A', 'N/A'],
        ['H_44', 70, True, 'Approching FIRST AVE', 'N/A'],
        ['H_45', 70, True, 'Welcome to FIRST AVE', '2'],
        ['I_46', 70, False, 'N/A', 'N/A'],
        ['I_47', 70, False, 'Approching STATION SQUARE', 'N/A'],
        ['I_48', 70, False, 'Welcome to STATION SQUARE', '2'],
        ['J_49', 60, False, 'N/A', 'N/A'],
        ['J_50', 60, False, 'N/A', 'N/A'],
        ['J_51', 55, False, 'N/A', 'N/A'],
        ['J_52', 55, False, 'N/A', 'N/A'],]
    
    b6 = [ ['J_53', 55, False, 'N/A', 'N/A'], #beacon6
        ['J_54', 55, False, 'N/A', 'N/A'],
        ['K_55', 55, False, 'N/A', 'N/A'],
        ['K_56', 55, False, 'N/A', 'N/A'],
        ['K_57', 55, False, 'N/A', 'N/A'],
        ['L_58', 55, False, 'N/A', 'N/A'],
        ['L_59', 55, False, 'Approching SOUTH HILLS JUNCTION', 'N/A'],
        ['L_60', 55, False, 'Welcome to SOUTH HILLS JUNCTION', '2'],
        ['M_61', 55, False, 'N/A', 'N/A'],
        ['M_62', 55, False, 'N/A', 'N/A'],
        ['M_63', 55, False, 'N/A', 'N/A'],
        ['N_64', 55, False, 'N/A', 'N/A'],
        ['N_65', 55, False, 'N/A', 'N/A'],
        ['N_66', 55, False, 'N/A', 'N/A'], ]
    
    b7 = [ ['J_52', 55, False, 'N/A', 'N/A'],
        ['J_51', 55, False, 'N/A', 'N/A'], #beacon7
        ['J_50', 60, False, 'N/A', 'N/A'],
        ['J_49', 60, False, 'Approching STATION SQUARE', 'N/A'],
        ['I_48', 70, False, 'Welcome to STATION SQUARE', '1'],
        ['I_47', 70, False, 'N/A', 'N/A'],
        ['I_46', 70, False, 'Approching FIRST AVE', 'N/A'],
        ['H_45', 70, True, 'Welcome to FIRST AVE', '1'],
        ['H_44', 70, True, 'N/A', 'N/A']
         ]
    
    b8 = [ ['O_67', 55, False, 'N/A', 'N/A'], #beacon8
        ['P_68', 55, False, 'N/A', 'N/A'],
        ['P_69', 55, True, 'N/A', 'N/A'],
        ['P_70', 55, True, 'N/A', 'N/A'],
        ['Q_71', 55, False, 'N/A', 'N/A'], ]
    
    b9 = [  ['H_38', 70, True, 'N/A', 'N/A'], #9
        ['H_37', 70, True, 'N/A', 'N/A'],
        ['H_36', 70, True, 'Approching STEEL PLAZA', 'N/A'],
        ['H_35', 70, True, 'Welcome to STEEL PLAZA' , '1'],
        ['H_34', 70, True, 'N/A', 'N/A'],
        ['H_33', 70, True, 'N/A', 'N/A'],
        ]
    
    b10 = [ ['R_72', 55, False, 'N/A', 'N/A'], # beacon
        ['S_73', 55, False, 'N/A', 'N/A'],
        ['S_74', 55, True, 'N/A', 'N/A'],
        ['S_75', 55, True, 'N/A', 'N/A'],
        ['T_76', 55, False, 'N/A', 'N/A'] ]
    
    b11 = [ ['H_27', 70, True, 'N/A', 'N/A'], #beacon
        ['H_26', 70, True, 'Approching PENN STATION', 'N/A'],
        ['H_25', 70, True, 'Welcome to PENN STATION', '1'],
        ['H_24', 70, False, 'N/A', 'N/A'],
        ['G_23', 55, False, 'N/A', 'N/A'],
        ['G_22', 55, False, 'Approching SWISSVILLE', 'N/A'],
        ['G_21', 55, False,'Welcome to SWISSVILLE', '2'],
        ['F_20', 70, False, 'N/A', 'N/A'],
        ['F_19', 70, False, 'N/A', 'N/A'],
        ['F_18', 70, False, 'N/A', 'N/A'],
        ['F_17', 55, False, 'Approching HERRON AVE', 'N/A'],
        ['F_16', 40, False, 'Welcome to HERRON AVE', '2'] ]
    
    b12 = [ ['A_1', 40, False, 'N/A', 'N/A'],  #end #beacon
        ['A_2', 40, False, 'N/A', 'N/A'],
        ['A_3', 40, False, 'N/A', 'N/A'],
        ['B_4', 40, False, 'N/A', 'N/A'],
        ['B_5', 40, False, 'N/A', 'N/A'],
        ['B_6', 40, False, 'Approching SHADYSIDE', 'N/A'],
        ['C_7', 40, False, 'Welcome to SHADYSIDE', '2'],
        ['C_8', 40, False, 'N/A', 'N/A'],
        ['C_9', 40, False, 'N/A', 'N/A'] ]
    

    b13 =[  # beacon
           ['E_15', 40, False, 'Approching HERRON AVE', 'N/A'],
           ['E_14', 40, False, 'N/A', 'N/A'],
           ['E_13', 40, False, 'N/A', 'N/A'],
           ['D_12', 40, False, 'N/A', 'N/A'],
           ['D_11', 40, False, 'N/A', 'N/A'],
           ['D_10', 40, False, 'N/A', 'N/A']
        ]
    
    b14 = [
            ['T_76', 55, False, 'N/A', 'N/A'], # beacon
            ['S_75', 55, True, 'N/A', 'N/A'],
            ['S_74', 55, True, 'N/A', 'N/A'],
            ['S_73', 55, False, 'N/A', 'N/A'],
            ['R_72', 55, False, 'N/A', 'N/A']
        ]
    
    b15 = [
            ['Q_71', 55, False, 'N/A', 'N/A'], # beacon
            ['P_70', 55, True, 'N/A', 'N/A'],
            ['P_69', 55, True, 'N/A', 'N/A'],
            ['P_68', 55, False, 'N/A', 'N/A'],
            ['O_67', 55, False, 'N/A', 'N/A']
        ]
    
    b17 = [
        ['J_52', 55, False, 'N/A', 'N/A'], # beacon
        ['N_66', 55, False, 'N/A', 'N/A'],
        ['N_65', 55, False, 'N/A', 'N/A'],
        ['N_64', 55, False, 'N/A', 'N/A'],
        ['M_63', 55, False, 'N/A', 'N/A'],
        ['M_62', 55, False, 'N/A', 'N/A'],
        ['M_61', 55, False, 'N/A', 'N/A'],
        ['L_60', 55, False, 'Welcome to SOUTH HILLS JUNCTION', '2'],
        ['L_59', 55, False, 'Approching SOUTH HILLS JUNCTION', 'N/A'],
        ['L_58', 55, False, 'N/A', 'N/A'],
        ['K_57', 55, False, 'N/A', 'N/A'],
        ['K_56', 55, False, 'N/A', 'N/A'],
        ['K_55', 55, False, 'N/A', 'N/A'],
        ['J_54', 55, False, 'N/A', 'N/A'],
        ['J_53', 55, False, 'N/A', 'N/A']
    ]

    b18 =[
    ['J_52', 55, False, 'N/A', 'N/A'], # beacon
    ['J_51', 55, False, 'N/A', 'N/A'],
    ['J_50', 60, False, 'N/A', 'N/A'],
    ['J_49', 60, False, 'N/A', 'N/A'],
    ['I_48', 70, False, 'Welcome to STATION SQUARE', '2'],
    ['I_47', 70, False, 'Approching STATION SQUARE', 'N/A'],
    ['I_46', 70, False, 'N/A', 'N/A'],
    ['H_45', 70, True, 'Welcome to FIRST AVE', '2'],
    ['H_44', 70, True, 'Approching FIRST AVE', 'N/A'],
    ['H_43', 70, True, 'N/A', 'N/A'],
    ['H_42', 70, True, 'N/A', 'N/A'],
    ['H_41', 70, True, 'N/A', 'N/A'],
    ['H_40', 70, True, 'N/A', 'N/A']
    ]

    b19 = [  ['H_32', 70, True, 'N/A', 'N/A'], # beacon
        ['H_31', 70, True, 'N/A', 'N/A'],
        ['H_30', 70, True, 'N/A', 'N/A'],
        ['H_29', 70, True, 'N/A', 'N/A'],
        ['H_28', 70, True, 'N/A', 'N/A']
    ]

    #def __init__(self):
        # self.TD = TempData()
        # self.current_staton = "yard"
        # self.next_station = "yard"

    #may be used if we need to tell next station from current station
    #def Get_Next_Station(self,line):
    
    def green_get_speed_lim(self,index):
        return self.green[index][1]
    
    def green_get_underground(self,index):
        return self.green[index][2]
        
    def get_green_station(self,index):
        return self.green[index][3]
    
    def get_green_door_side(self,index):
        return self.green[index][4]

    def red_get_speed_lim(self,index):
        return self.red[index][1]
    
    def red_get_underground(self,index):
        return self.red[index][2]
    
    def get_red_station(self,index):
        return self.red[index][3]
    
    def get_red_door_side(self,index):
        return self.red[index][4]
        
