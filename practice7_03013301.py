# -*- coding: utf-8 -*- 
'''
Created on 2016年6月2日

@author: wanglu
'''
import unittest
from iapws import IAPWS97
from iapws.iapws97 import (_Backward1_T_Ph,_Backward1_T_Ps,_Backward2_T_Ph,_Backward2_T_Ps,
_Region3,_Backward3_T_Ph,_Backward3_v_Ph,_Backward3_T_Ps,_Backward3_v_Ps)

#Unit Test for Region1
class Region1Test(unittest.TestCase):
    def setUp(self):
        # IF97-Rev,Table 5 Page 9 : p,t(K),h,s
        self.tab5=[[ 3, 300, 0.115331273e3, 0.392294792 ],
                   [80, 300, 0.184142828e3, 0.368563852 ],
                   [ 3, 500, 0.975542239e3, 0.258041912e1]]
        
        # IF97-Rev,Table 7 Page 11 : p,h,T
        self.tab7=[[ 3, 500, 0.391798509e3 ],
                   [80, 500, 0.378108626e3 ],
                   [80,1500, 0.611041229e3 ]]
        
        # IF97-Rev,Table 9 Page 12 : p,s,T
        self.tab9=[[ 3, 0.5, 0.307842258e3],
                   [80, 0.5, 0.309979785e3],
                   [80,   3, 0.565899909e3]]
        
    def testSpecificEnthalpyPT(self):
        places = 6
        for item in  self.tab5:
            result = IAPWS97(P=item[0], T=item[1])
            self.assertAlmostEqual(result.h,item[2],places)

    def testSpecificEntropyPT(self):
        places = 8
        for item in  self.tab5:
            result = IAPWS97(P=item[0], T=item[1])
            self.assertAlmostEqual(result.s,item[3],places)
    
    def testEquation11_T_ph(self):
        places = 6
        for item in self.tab7:
            result = _Backward1_T_Ph(item[0], item[1])
            self.assertAlmostEqual(result, item[2], places)
            
    def testEquation9_T_p_s(self):
        places = 6
        for item in self.tab9:
            result = _Backward1_T_Ps(item[0], item[1])
            self.assertAlmostEqual(result, item[2], places)


#Unit Test for Region2
class Region2Test(unittest.TestCase):
    def setUp(self):
        # IF97-Rev, Eq15, Table 15 Page 17 : p,t(K),h,s
        self.tab15=[[0.0035, 300, 0.254991145e4, 0.852238967e1],
                    [0.0035, 700, 0.333568375e4, 0.101749996e2],
                    [    30, 700, 0.263149474e4, 0.517540298e1]]
        
        # IF97-Rev, Eq22~24, Table 24 Page 25 : p,h,T
        self.tab24=[[0.001, 3000, 0.534433241e3],
                    [    3, 3000, 0.575373370e3],
                    [    3, 4000, 0.101077577e4],
                    [ 5, 3500, 0.801299102e3],
                    [ 5, 4000, 0.101531583e4],
                    [25, 3500, 0.875279054e3],
                    [ 40, 2700, 0.743056411e3],
                    [ 60, 2700, 0.791137067e3],
                    [ 60, 3200, 0.882756860e3]]
        
        # IF97-Rev, Eq25~27, Table 29 Page 29 : p,s,T
        self.tab29=[[0.1, 7.5, 0.399517097e3],
                    [0.1,   8, 0.514127081e3],
                    [2.5,   8, 0.103984917e4],
                    [ 8,   6, 0.600484040e3],
                    [ 8, 7.5, 0.106495556e4],
                    [90,   6, 0.103801126e4],
                    [ 20, 5.75, 0.697992849e3],
                    [ 80, 5.25, 0.854011484e3],
                    [ 80, 5.75, 0.949017998e3]]
        
    def testEq15PT2h(self):
        places = 5
        for item in  self.tab15:
            result = IAPWS97(P=item[0], T=item[1])
            self.assertAlmostEqual(result.h,item[2],places)

    def testEq15PT2s(self):
        places = 6
        for item in  self.tab15:
            result = IAPWS97(P=item[0], T=item[1])
            self.assertAlmostEqual(result.s,item[3],places)
            
    def testBk2PH2T(self):
        places = 5
        for item in  self.tab24:
            result = _Backward2_T_Ph(item[0], item[1])
            self.assertAlmostEqual(result,item[2],places)
    
    def testBk2Ps2T(self):
        places = 5
        for item in  self.tab29:
            result = _Backward2_T_Ps(item[0], item[1])
            self.assertAlmostEqual(result,item[2],places)

            
#Unit Test for Region3
class Region3Test(unittest.TestCase):
    def setUp(self):
        # IF97-Rev,Table 33 Page 32 : rho,T,p,h,s
        self.tab33=[[500, 650, 0.255837018e2, 0.186343019e4, 0.405427273e1 ],
                    [200, 650, 0.222930643e2, 0.237512401e4, 0.485438792e1 ],
                    [500, 750, 0.783095639e2, 0.225868845e4, 0.446971906e1]]
        
    def testEq28_rhoT2P(self):
        places = 6
        for item in self.tab33:
            result = _Region3(item[0], item[1])
            self.assertAlmostEqual(result['P'], item[2], places)
            
    def testEq28_rhoT2h(self):
        places = 4
        for item in self.tab33:
            result = _Region3(item[0], item[1])
            self.assertAlmostEqual(result['h'], item[3], places)
    
    def testEq28_rhoT2s(self):
        places = 7
        for item in self.tab33:
            result = _Region3(item[0], item[1])
            self.assertAlmostEqual(result['s'], item[4], places)

#Unit Test for Supplementary Equation（based on “Supp-Tv(ph,ps)3-2014.pdf”）
class SuppTest(unittest.TestCase):
    def setUp(self):
        # Supp-Tv(ph,ps)3-2014,Table 5 Page 8 : p,h,T
        self.tab5=[[20, 1700, 6.293083892e2],
                   [50, 2000, 6.905718338e2],
                   [100,2100, 7.336163014e2],
                   [20, 2500, 6.418418053e2],
                   [50, 2400, 7.351848618e2],
                   [100,2700, 8.420460876e2]]
        
        # Supp-Tv(ph,ps)3-2014,Table 8 Page 10 : p,h,V
        self.tab8=[[ 20, 1700, 1.749903962e-3],
                   [ 50, 2000, 1.908139035e-3],
                   [100, 2100, 1.676229776e-3],
                   [ 20, 2500, 6.670547043e-3],
                   [ 50, 2400, 2.801244590e-3],
                   [100, 2700, 2.404234998e-3]]
        
        # Supp-Tv(ph,ps)3-2014,Table 12 Page 13 : p,s,t
        self.tab12=[[ 20, 3.8, 6.282959869e2],
                    [ 50, 3.6, 6.297158726e2],
                    [100, 4.0, 7.056880237e2],
                    [ 20, 5.0, 6.401176443e2],
                    [ 50, 4.5, 7.163687517e2],
                    [100, 5.0, 8.474332825e2]]
        
        # Supp-Tv(ph,ps)3-2014,Table 15 Page 15 : p,s,V
        self.tab15=[[ 20, 3.8, 1.733791463e-3],
                    [ 50, 3.6, 1.469680170e-3],
                    [100, 4.0, 1.555893131e-3],
                    [ 20, 5.0, 6.262101987e-3],
                    [ 50, 4.5, 2.332634294e-3],
                    [100, 5.0, 2.449610757e-3]]
        
        
    def testSupp_ph2T(self):
        places = 7
        for item in self.tab5:
            t = _Backward3_T_Ph(item[0], item[1])
            self.assertAlmostEqual(t, item[2], places)
            
    def testSupp_ph2v(self):
        places = 12
        for item in self.tab8:
            v = _Backward3_v_Ph(item[0], item[1])
            self.assertAlmostEqual(v, item[2], places)
            
    def testSupp_ps2T(self):
        places = 7
        for item in self.tab12:
            t = _Backward3_T_Ps(item[0], item[1])
            self.assertAlmostEqual(t, item[2], places)
            
    def testSupp_ps2v(self):
        places = 12
        for item in self.tab15:
            v = _Backward3_v_Ps(item[0], item[1])
            self.assertAlmostEqual(v, item[2], places)

#Unit Test Suite
def mainTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Region1Test))
    suite.addTest(unittest.makeSuite(Region2Test))
    suite.addTest(unittest.makeSuite(Region3Test))
    suite.addTest(unittest.makeSuite(SuppTest))
    return suite

#Main Function
if __name__ == '__main__':
    unittest.main(defaultTest='mainTestSuite')    