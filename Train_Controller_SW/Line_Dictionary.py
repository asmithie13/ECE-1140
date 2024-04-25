import CTC
from CTC import CTC_TrackData

class Line_Dictionary():

    ##start
    green = [
        ['K_63', 70, False, '', ''],
        ['K_64', 70, False, 'Approching GLENBURY', ''],
        ['K_65', 70, False, 'Welcome to GLENBURY', '1'],
        ['K_66', 70, False, '', ''],
        ['K_67', 40, False, '', ''],
        ['K_68', 40, False, '', ''],
        ['L_69', 40, False, '', ''],
        ['L_70', 40, False, '', ''],
        ['L_71', 40, False, '', ''],
        ['L_72', 40, False, 'Approching DORMONT', ''],
        ['L_73', 40, False, 'Welcome to DORMONT', '1'],
        ['M_74', 40, False, '', ''],
        ['M_75', 40, False, '', ''],
        ['M_76', 40, False, 'APPROACHING MT LEBANON', ''],
        ['N_77', 70, False, 'Welcome to MT LEBANON', '1'],
        ['N_78', 70, False, '', ''],
        ['N_79', 70, False, '', ''],
        ['N_80', 70, False, '', ''],
        ['N_81', 70, False, '', ''],
        ['N_82', 70, False, '', ''],
        ['N_83', 70, False, '', ''],
        ['N_84', 70, False, '', ''],
        ['N_85', 70, False, '', ''],
        ['O_86', 25, False, '', ''],
        ['O_87', 25, False, 'Approching POPLAR', ''],
        ['O_88', 25, False, 'Welcome to POPLAR', '2'],
        ['P_89', 25, False, '', ''],
        ['P_90', 25, False, '', ''],
        ['P_91', 25, False, '', ''],
        ['P_92', 25, False, '', ''],
        ['P_93', 25, False, '', ''],
        ['P_94', 25, False, '', ''],
        ['P_95', 25, False, 'Approching CASTLE SHANNON', ''],
        ['P_96', 25, False, 'Welcome to CASTLE SHANNON', '2'],
        ['P_97', 25, False, '', ''],
        ['Q_98', 25, False, '', ''],
        ['Q_99', 25, False, '', ''],
        ['Q_100', 25, False, '', ''],	#change dir
        ['N_85', 70, False, '', ''],
        ['N_84', 70, False, '', ''],
        ['N_83', 70, False, '', ''],
        ['N_82', 70, False, '', ''],
        ['N_81', 70, False, '', ''],
        ['N_80', 70, False, '', ''],
        ['N_79', 70, False, '', ''],
        ['N_78', 70, False, 'Approching MT LEBANON', ''],
        ['N_77', 70, False, 'Welcome to MT LEBANON', '2'],
        ['R_101', 26, False, '', ''], #new section
        ['S_102', 28, False, '', ''],
        ['S_103', 28, False, '', ''],
        ['S_104', 28, False, 'Approching DORMONT', ''],
        ['T_105', 28, False, 'Welcome to DORMONT', '1'],
        ['T_106', 28, False, '', ''],
        ['T_107', 28, False, '', ''],
        ['T_108', 28, False, '', ''],
        ['T_109', 28, False, '', ''],
        ['U_110', 30, False, '', ''],
        ['U_111', 30, False, '', ''],
        ['U_112', 30, False, '', ''],
        ['U_113', 30, False, 'Approaching GLENBURY', ''],
        ['U_114', 30, False, 'Welcome to GLENBURY', '1'],
        ['U_115', 30, False, '', ''],
        ['U_116', 30, False, '', ''],
        ['V_117', 15, False, '', ''],
        ['V_118', 15, False, '', ''],
        ['V_119', 15, False, '', ''],
        ['V_120', 15, False, '', ''],
        ['V_121', 15, False, '', ''],
        ['W_122', 20, True, 'Approaching OVERBROOK', ''],
        ['W_123', 20, True, 'Welcome to OVERBROOK', '1'],
        ['W_124', 20, True, '', ''],
        ['W_125', 20, True, '', ''],
        ['W_126', 20, True, '', ''],
        ['W_127', 20, True, '', ''],
        ['W_128', 20, True, '', ''],
        ['W_129', 20, True, '', ''],
        ['W_130', 20, True, '', ''],
        ['W_131', 20, True, 'Apporaching INGLEWOOD', ''],
        ['W_132', 20, True, 'Welcome to INGLEWOOD', '2'],
        ['W_133', 20, True, '', ''],
        ['W_134', 20, True, '', ''],
        ['W_135', 20, True, '', ''],
        ['W_136', 20, True, '', ''],
        ['W_137', 20, True, '', ''],
        ['W_138', 20, True, '', ''],
        ['W_139', 20, True, '', ''],
        ['W_140', 20, True, 'Approaching CENTRAL', ''],
        ['W_141', 20, True, 'Welcome to CENTRAL', '1'],
        ['W_142', 20, True, '', ''],
        ['W_143', 20, True, '', ''],
        ['X_144', 20, False, '', ''],
        ['X_145', 20, False, '', ''],
        ['X_146', 20, False, '', ''],
        ['Y_147', 20, False, '', ''],
        ['Y_148', 20, False, '', ''],
        ['Y_149', 20, False, '', ''],
        ['Z_150', 20, False, '', ''],
        ['F_28', 30, False, '', ''],
        ['F_27', 30, False, '', ''],
        ['F_26', 70, False, '', ''],
        ['F_25', 70, False, '', ''],
        ['F_24', 70, False, '', ''],
        ['F_23', 70, False, 'Apporaching WHITED', ''],
        ['F_22', 70, False, 'Welcome to WHITED', '1'],
        ['F_21', 70, False, '', ''],
        ['E_20', 60, False, '', ''],
        ['E_19', 60, False, '', ''],
        ['E_18', 60, False, '', ''],
        ['E_17', 60, False, 'Approaching STATION', ''],
        ['D_16', 70, False, 'Welcome to Station', '1'], 
        ['D_15', 70, False, '', ''],
        ['D_14', 70, False, '', ''],
        ['D_13', 70, False, '', ''],
        ['C_12', 45, False, '', ''],
        ['C_11', 45, False, '', ''],
        ['C_10', 45, False, 'Apporaching EDGEBROOK', ''],
        ['C_9', 45, False, 'Welcome to EDGEBROOK', '2'],
        ['C_8', 45, False, '', ''],
        ['C_7', 45, False, '', ''],
        ['B_6', 45, False, '', ''],
        ['B_5', 45, False, '', ''],
        ['B_4', 45, False, '', ''],
        ['A_3', 45, False, 'Approching PINONEER', ''],
        ['A_2', 45, False, 'PIONEER', '2'],
        ['A_1', 45, False, '', ''],
        ['D_13', 70, False, '', ''], #new section
        ['D_14', 70, False, '', ''],
        ['D_15', 70, False, 'Apporaching STATION', ''],
        ['D_16', 70, False, 'Welcome to STATION', '2'],
        ['E_17', 60, False, '', ''],
        ['E_18', 60, False, '', ''],
        ['E_19', 60, False, '', ''],
        ['E_20', 60, False, '', ''],
        ['F_21', 70, False, 'Apporaching WHITED', ''],
        ['F_22', 70, False, 'Welcome to WHITED', '2'],
        ['F_23', 70, False, '', ''],
        ['F_24', 70, False, '', ''],
        ['F_25', 70, False, '', ''],
        ['F_26', 70, False, '', ''],
        ['F_27', 30, False, '', ''],
        ['F_28', 30, False, '', ''],
        ['G_29', 30, False, '', ''],
        ['G_30', 30, False, 'Apporaching SOUTH BANK', ''],
        ['G_31', 30, False, 'Welcome to SOUTH BANK', '2'],
        ['G_32', 30, False, '', ''],
        ['H_33', 30, False, '', ''],
        ['H_34', 30, False, '', ''],
        ['H_35', 30, False, '', ''],
        ['I_36', 30, True, '', ''],
        ['I_37', 30, True,'Apporachning CENTRAL', ''],
        ['I_38', 30, True,'Welcome to CENTRAL', ''],
        ['I_39', 30, True,'' , '1'],
        ['I_40', 30, True, '', ''],
        ['I_41', 30, True, '', ''],
        ['I_42', 30, True, '', ''],
        ['I_43', 30, True, '', ''],
        ['I_44', 30, True, '', ''],
        ['I_45', 30, True, '', ''],
        ['I_46', 30, True, 'Apporaching INGLEWOOD', ''],
        ['I_47', 30, True,'Welcome to INGLEWOOD' , ''],
        ['I_48', 30, True,'' , '1'],
        ['I_49', 30, True, '', ''],
        ['I_50', 30, True, '', ''],
        ['I_51', 30, True, '', ''],
        ['I_52', 30, True, '', ''],
        ['I_53', 30, True, '', ''],
        ['I_54', 30, True, '', ''],
        ['I_55', 30, True, 'Approaching OVERBROOK', ''],
        ['I_56', 30, True, 'Welcome to OVERBROOK', ''],
        ['I_57', 30, True, '', '1'],
        ['I_58', 30, True, '', '1']
    ]
    green_station = ["Glenbury", 
                     "Dormont", 
                     "Mt Lebanon",
                     "Poplar",
                     "Castle Shannon",
                     "Mt Lebanon",
                     "Dormont",
                     "Glenbury",
                     "Overbrook",
                     "Inglewood",
                     "Central",
                     "Whited",
                     "Station",
                     "Edgebrook",
                     "Pioneer",
                     "Station",
                     "Whited",
                     "South Bank",
                     "Central",
                     "Inglewood",
                     "Overbrook",
                     "Yard"]
    
    red_station =  ["Herron",
     "Swissvile",
     "Penn Station",
     "Steel Plaza",
     "First Ave",
     "Station Square",
     "South Hills",
     "Station Square",
     "First Ave",
     "Steel Plaza",
     "Penn Station",
     "Swissville",
     "Herron",
     "Shadyside",
     "Yard"]

    red = [
        ['D_10', 40, False, '', ''],
        ['D_11', 40, False, '', ''],
        ['D_12', 40, False, '', ''],
        ['E_13', 40, False, '', ''],
        ['E_14', 40, False, '', ''],
        ['E_15', 40, False, 'Approching HERRON AVE', ''],
        ['F_16', 40, False, 'Welcome to HERRON AVE', '1'],
        ['F_17', 55, False, '', ''],
        ['F_18', 70, False, '', ''],
        ['F_19', 70, False, '', ''],
        ['F_20', 70, False, 'Approching HERRON AVE', ''],
        ['G_21', 55, False, 'Welcome to SWISSVILLE', '1'],
        ['G_22', 55, False, '', ''],
        ['G_23', 55, False, '', ''],
        ['H_24', 70, False, 'Approching PENN STATION', ''],
        ['H_25', 70, True, 'Welcome to PENN STATION', '2'],
        ['H_26', 70, True, '', ''],
        ['H_27', 70, True, '', ''],
        ['H_28', 70, True, '', ''],
        ['H_29', 70, True, '', ''],
        ['H_30', 70, True, '', ''],
        ['H_31', 70, True, '', ''],
        ['H_32', 70, True, '', ''],
        ['H_33', 70, True, '', ''],
        ['H_34', 70, True, 'Approching STEEL PLAZA', ''],
        ['H_35', 70, True, 'Welcome to STEEL PLAZA', '2'],
        ['H_36', 70, True, '', ''],
        ['H_37', 70, True, '', ''],
        ['H_38', 70, True, '', ''],
        ['H_39', 70, True, '', ''],
        ['H_40', 70, True, '', ''],
        ['H_41', 70, True, '', ''],
        ['H_42', 70, True, '', ''],
        ['H_43', 70, True, '', ''],
        ['H_44', 70, True, 'Approching FIRST AVE', ''],
        ['H_45', 70, True, 'Welcome to FIRST AVE', '2'],
        ['I_46', 70, False, '', ''],
        ['I_47', 70, False, 'Approching STATION SQUARE', ''],
        ['I_48', 70, False, 'Welcome to STATION SQUARE', '2'],
        ['J_49', 60, False, '', ''],
        ['J_50', 60, False, '', ''],
        ['J_51', 55, False, '', ''],
        ['J_52', 55, False, '', ''],
        ['J_53', 55, False, '', ''],
        ['J_54', 55, False, '', ''],
        ['K_55', 55, False, '', ''],
        ['K_56', 55, False, '', ''],
        ['K_57', 55, False, '', ''],
        ['L_58', 55, False, '', ''],
        ['L_59', 55, False, 'Approching SOUTH HILLS JUNCTION', ''],
        ['L_60', 55, False, 'Welcome to SOUTH HILLS JUNCTION', '2'],
        ['M_61', 55, False, '', ''],
        ['M_62', 55, False, '', ''],
        ['M_63', 55, False, '', ''],
        ['N_64', 55, False, '', ''],
        ['N_65', 55, False, '', ''],
        ['N_66', 55, False, '', ''],
        ['J_52', 55, False, '', ''],
        ['J_51', 55, False, '', ''],
        ['J_50', 60, False, '', ''],
        ['J_49', 60, False, 'Approching STATION SQUARE', ''],
        ['I_48', 70, False, 'Welcome to STATION SQUARE', '1'],
        ['I_47', 70, False, '', ''],
        ['I_46', 70, False, 'Approching FIRST AVE', ''],
        ['H_45', 70, True, 'Welcome to FIRST AVE', '1'],
        ['H_44', 70, True, '', ''],
        ['H_43', 70, True, '', ''],
        ['O_67', 55, False, '', ''], #segment 1
        ['P_68', 55, False, '', ''],
        ['P_69', 55, True, '', ''],
        ['P_70', 55, True, '', ''],
        ['Q_71', 55, False, '', ''],
        ['H_38', 70, True, '', ''],
        ['H_37', 70, True, '', ''],
        ['H_36', 70, True, 'Approching STEEL PLAZA', ''],
        ['H_35', 70, True, 'Welcome to STEEL PLAZA' , '1'],
        ['H_34', 70, True, '', ''],
        ['H_33', 70, True, '', ''],
        ['H_32', 70, True, '', ''],
        ['R_72', 55, False, '', ''], # segment 2
        ['S_73', 55, False, '', ''],
        ['S_74', 55, True, '', ''],
        ['S_75', 55, True, '', ''],
        ['T_76', 55, False, '', ''],

        ['H_27', 70, True, '', ''],
        ['H_26', 70, True, 'Approching PENN STATION', ''],
        ['H_25', 70, True, 'Welcome to PENN STATION', '1'],
        ['H_24', 70, False, '', ''],
        ['G_23', 55, False, '', ''],
        ['G_22', 55, False, 'Approching SWISSVILLE', ''],
        ['G_21', 55, False,'Welcome to SWISSVILLE', '2'],
        ['F_20', 70, False, '', ''],
        ['F_19', 70, False, '', ''],
        ['F_18', 70, False, '', ''],
        ['F_17', 55, False, 'Approching HERRON AVE', ''],
        ['F_16', 40, False, 'Welcome to HERRON AVE', '2'],
        ['A_1', 40, False, '', ''],  #end
        ['A_2', 40, False, '', ''],
        ['A_3', 40, False, '', ''],
        ['B_4', 40, False, '', ''],
        ['B_5', 40, False, '', ''],
        ['B_6', 40, False, 'Approching SHADYSIDE', ''],
        ['C_7', 40, False, 'Welcome to SHADYSIDE', '2'],
        ['C_8', 40, False, '', ''],
        ['C_9', 40, False, '', '']
    ]


    b1 = [ ['D_10', 40, False, '', ''], #beacon
        ['D_11', 40, False, '', ''],
        ['D_12', 40, False, '', ''],
        ['E_13', 40, False, '', ''],
        ['E_14', 40, False, '', ''],
        ['E_15', 40, False, 'Approching HERRON AVE', ''], ]
    
    b2 = [ ['F_16', 40, False, 'Welcome to HERRON AVE', '1'],
        ['F_17', 55, False, '', ''], #beacon
        ['F_18', 70, False, '', ''],
        ['F_19', 70, False, '', ''],
        ['F_20', 70, False, 'Approching SWISSVILLE', ''],
        ['G_21', 55, False, 'Welcome to SWISSVILLE', '1'],
        ['G_22', 55, False, '', ''],
        ['G_23', 55, False, '', ''],
        ['H_24', 70, False, 'Approching PENN STATION', ''],
        ['H_25', 70, True, 'Welcome to PENN STATION', '2'],
        ['H_26', 70, True, '', ''],
        ['H_27', 70, True, '', '']
 ]
    
    b3 = [ ['H_28', 70, True, '', ''], #beacon3
        ['H_29', 70, True, '', ''],
        ['H_30', 70, True, '', ''],
        ['H_31', 70, True, '', ''],
        ['H_32', 70, True, '', '']]
    
    b4 = [ 
        ['H_33', 70, True, '', ''],
        ['H_34', 70, True, 'Approching STEEL PLAZA', ''], #beacon
        ['H_35', 70, True, 'Welcome to STEEL PLAZA', '2'],
        ['H_36', 70, True, '', ''],
        ['H_37', 70, True, '', ''],
        ['H_38', 70, True, '', ''],
    ]

    
    b5 = [ ['H_39', 70, True, '', ''], #b5
        ['H_40', 70, True, '', ''],
        ['H_41', 70, True, '', ''],
        ['H_42', 70, True, '', ''],
        ['H_43', 70, True, '', ''],
        ['H_44', 70, True, 'Approching FIRST AVE', ''],
        ['H_45', 70, True, 'Welcome to FIRST AVE', '2'],
        ['I_46', 70, False, '', ''],
        ['I_47', 70, False, 'Approching STATION SQUARE', ''],
        ['I_48', 70, False, 'Welcome to STATION SQUARE', '2'],
        ['J_49', 60, False, '', ''],
        ['J_50', 60, False, '', ''],
        ['J_51', 55, False, '', ''],
        ['J_52', 55, False, '', ''],]
    
    b6 = [ ['J_53', 55, False, '', ''], #beacon6
        ['J_54', 55, False, '', ''],
        ['K_55', 55, False, '', ''],
        ['K_56', 55, False, '', ''],
        ['K_57', 55, False, '', ''],
        ['L_58', 55, False, '', ''],
        ['L_59', 55, False, 'Approching SOUTH HILLS JUNCTION', ''],
        ['L_60', 55, False, 'Welcome to SOUTH HILLS JUNCTION', '2'],
        ['M_61', 55, False, '', ''],
        ['M_62', 55, False, '', ''],
        ['M_63', 55, False, '', ''],
        ['N_64', 55, False, '', ''],
        ['N_65', 55, False, '', ''],
        ['N_66', 55, False, '', ''], ]
    
    b7 = [ ['J_52', 55, False, '', ''],
        ['J_51', 55, False, '', ''], #beacon7
        ['J_50', 60, False, '', ''],
        ['J_49', 60, False, 'Approching STATION SQUARE', ''],
        ['I_48', 70, False, 'Welcome to STATION SQUARE', '1'],
        ['I_47', 70, False, '', ''],
        ['I_46', 70, False, 'Approching FIRST AVE', ''],
        ['H_45', 70, True, 'Welcome to FIRST AVE', '1'],
        ['H_44', 70, True, '', '']
         ]
    
    b8 = [ ['O_67', 55, False, '', ''], #beacon8
        ['P_68', 55, False, '', ''],
        ['P_69', 55, True, '', ''],
        ['P_70', 55, True, '', ''],
        ['Q_71', 55, False, '', ''], ]
    
    b9 = [  ['H_38', 70, True, '', ''], #9
        ['H_37', 70, True, '', ''],
        ['H_36', 70, True, 'Approching STEEL PLAZA', ''],
        ['H_35', 70, True, 'Welcome to STEEL PLAZA' , '1'],
        ['H_34', 70, True, '', ''],
        ['H_33', 70, True, '', ''],
        ]
    
    b10 = [ ['R_72', 55, False, '', ''], # beacon
        ['S_73', 55, False, '', ''],
        ['S_74', 55, True, '', ''],
        ['S_75', 55, True, '', ''],
        ['T_76', 55, False, '', ''] ]
    
    b11 = [ ['H_27', 70, True, '', ''], #beacon
        ['H_26', 70, True, 'Approching PENN STATION', ''],
        ['H_25', 70, True, 'Welcome to PENN STATION', '1'],
        ['H_24', 70, False, '', ''],
        ['G_23', 55, False, '', ''],
        ['G_22', 55, False, 'Approching SWISSVILLE', ''],
        ['G_21', 55, False,'Welcome to SWISSVILLE', '2'],
        ['F_20', 70, False, '', ''],
        ['F_19', 70, False, '', ''],
        ['F_18', 70, False, '', ''],
        ['F_17', 55, False, 'Approching HERRON AVE', ''],
        ['F_16', 40, False, 'Welcome to HERRON AVE', '2'] ]
    
    b12 = [ ['A_1', 40, False, '', ''],  #end #beacon
        ['A_2', 40, False, '', ''],
        ['A_3', 40, False, '', ''],
        ['B_4', 40, False, '', ''],
        ['B_5', 40, False, '', ''],
        ['B_6', 40, False, 'Approching SHADYSIDE', ''],
        ['C_7', 40, False, 'Welcome to SHADYSIDE', '2'],
        ['C_8', 40, False, '', ''],
        ['C_9', 40, False, '', ''] ]
    

    b13 =[  # beacon
           ['E_15', 40, False, 'Approching HERRON AVE', ''],
           ['E_14', 40, False, '', ''],
           ['E_13', 40, False, '', ''],
           ['D_12', 40, False, '', ''],
           ['D_11', 40, False, '', ''],
           ['D_10', 40, False, '', '']
        ]
    
    b14 = [
            ['T_76', 55, False, '', ''], # beacon
            ['S_75', 55, True, '', ''],
            ['S_74', 55, True, '', ''],
            ['S_73', 55, False, '', ''],
            ['R_72', 55, False, '', '']
        ]
    
    b15 = [
            ['Q_71', 55, False, '', ''], # beacon
            ['P_70', 55, True, '', ''],
            ['P_69', 55, True, '', ''],
            ['P_68', 55, False, '', ''],
            ['O_67', 55, False, '', '']
        ]
    
    b17 = [
        ['J_52', 55, False, '', ''], # beacon
        ['N_66', 55, False, '', ''],
        ['N_65', 55, False, '', ''],
        ['N_64', 55, False, '', ''],
        ['M_63', 55, False, '', ''],
        ['M_62', 55, False, '', ''],
        ['M_61', 55, False, '', ''],
        ['L_60', 55, False, 'Welcome to SOUTH HILLS JUNCTION', '2'],
        ['L_59', 55, False, 'Approching SOUTH HILLS JUNCTION', ''],
        ['L_58', 55, False, '', ''],
        ['K_57', 55, False, '', ''],
        ['K_56', 55, False, '', ''],
        ['K_55', 55, False, '', ''],
        ['J_54', 55, False, '', ''],
        ['J_53', 55, False, '', '']
    ]

    b18 =[
    ['J_52', 55, False, '', ''], # beacon
    ['J_51', 55, False, '', ''],
    ['J_50', 60, False, '', ''],
    ['J_49', 60, False, '', ''],
    ['I_48', 70, False, 'Welcome to STATION SQUARE', '2'],
    ['I_47', 70, False, 'Approching STATION SQUARE', ''],
    ['I_46', 70, False, '', ''],
    ['H_45', 70, True, 'Welcome to FIRST AVE', '2'],
    ['H_44', 70, True, 'Approching FIRST AVE', ''],
    ['H_43', 70, True, '', ''],
    ['H_42', 70, True, '', ''],
    ['H_41', 70, True, '', ''],
    ['H_40', 70, True, '', '']
    ]

    b19 = [  ['H_32', 70, True, '', ''], # beacon
        ['H_31', 70, True, '', ''],
        ['H_30', 70, True, '', ''],
        ['H_29', 70, True, '', ''],
        ['H_28', 70, True, '', '']
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
        
