""" compare how the elements behave
 
We create a folder ground truth that possess the same thing than the other in a form of a dictionnary containing nparrays and other info.
the other files contains every test and the name is the date of the test
 
See Also
------------
 
Link 
 
"""
#\package Caiman/self.comparison
#\image html X.jpg
#\version   1.0
#\copyright GNU General Public License v2.0
#\date Created on Tue Jun 30 21:01:17 2015
#\author: jeremie KALFON


import platform as plt
import datetime
import numpy as np
    
"""
   Comparison(object): class you instanciate to compare the different functions you are calling in your program.
 
   Here it has been made for 3 different functions. for it to compare well you need to set your 
   ground truth with the same computer with which you are comparing the files
 
    
 
    Attributes
    ----------
    self : object
        see the linked image
 
    Methods
    -------
    __init__()
        Initialize the function be instanciating a comparison object  
        
    save(istruth)
        save the comparison object on a file
   
    See Also
    --------
    
    .. image:: /Users/jeremie/CaImAn/dev/kalfon/img/datacomparison.png
    """
class Comparison(object):

    def __init__(self):
        
        self.comparison ={'rig_shifts': {},
             'pwrig_shifts': {},
             'cnmf_on_patch': {},
             'cnmf_full_frame': {},    
        }
    
        self.comparison['rig_shifts']={
                           'ourdata': None,
                          'timer': None,
                          'sensibility': 0.001    #the sensibility USER TO CHOOSE
                         }
        self.comparison['pwrig_shifts']={
                          'ourdata': None,
                          'timer': None,
                          'sensibility': 0.001
                         }
        self.comparison['cnmf_on_patch']={
                          'ourdata': None,
                          'timer': None,
                          'sensibility': 0.01
                         }
        self.comparison['cnmf_full_frame']={
                          'ourdata': None,
                          'timer': None,
                          'sensibility': 0.01
                         }
        
    def save(self, istruth=False):
        """save the comparison object on a file
 
 
            depending on if we say this file will be ground truth or not, it wil be saved in either the tests or the groung truth folder
            if saved in test, a comparison to groundtruth will be add to the object 
            this comparison will be on 
                data : a normized difference of the normalized value of the arrays
                time : difference
 
            Parameters
            -----------
 
            self:  dictionnary
               the object of this class tha tcontains every value
            istruth: Boolean
                if we want it ot be the ground truth
             
            	See Also
            	---------
            
             
            	.. image:: /Users/jeremie/CaImAn/dev/kalfon/img/datacomparison.png
            
             
                """
#\bug       
#\warning 

        
        #we get the informetion of the computer
        dt = datetime.datetime.today()
        dt=str(dt)
        plat=plt.platform()
        plat=str(plat)
        pro=plt.processor()
        pro=str(pro)
        #we store a big file which is containing everything ( INFORMATION)
        self.information ={
                'platform': plat,
                'processor':pro,
                'values':self.comparison
                }
        #if we want to set this data as truth
        if istruth:
                #we just save it
               np.savez('/Users/jeremie/CaImAn/comparison/groundtruth.npz', **self.information)
               print('we now have ground truth')
        else:
            #if not we create a comparison first
            try: 
                with np.load('/Users/jeremie/CaImAn/comparison/groundtruth.npz') as data: 
        #if not we save the value of the difference into 
        #for rigid
        
        
                   A = data['values']['rig_shifts']['ourdata'][()] #we do this [()] because of REASONS
                   B = self.comparison['rig_shifts']['ourdata']
                   A = np.linalg.norm(A-B)/np.linalg.norm(A)
                   B = A < self.comparison['rig_shifts']['sensibility']
                   self.information['values']['rig_shifts'].update({'isdifferent':B,
                                          'diff_data': A,
                                          'diff_timing': data['ground_truth']['rig_shifts']['timer']
                                          - self.comparison['rig_shifts']['timer']
                                        
                                })
        #for pwrigid
                   A= data['values']['pwrig_shifts']['ourdata'][0][()]
                   B = self.comparison['pwrig_shifts']['ourdata'][0]
                   C = np.linalg.norm(A-B)/np.linalg.norm(A)
                   #there is xs and ys
                   A= data['values']['pwrig_shifts']['ourdata'][1][()]
                   B = self.comparison['pwrig_shifts']['ourdata'][1]
                   #a simple comparison algo
                   A = np.linalg.norm(A-B)/np.linalg.norm(A)
                   #we add both errors
                   A=A+C
                   B = A < self.comparison['pwrig_shifts']['sensibility']
                   self.information['values']['pwrig_shifts'].update({'isdifferent':B,
                                            'diff_data': A,
                                            'diff_timing': data['values']['pwrig_shifts']['timer']
                                            - self.comparison['pwrig_shifts']['timer']
                                        
                                })
        #for cnmf on patches 
                   A= data['values']['cnmf_on_patch']['ourdata'][0][()]
                   B = self.comparison['cnmf_on_patch']['ourdata'][0]
                   C = np.linalg.norm(A-B)/np.linalg.norm(A)
                   #there is temporal and spatial
                   A= data['values']['cnmf_on_patch']['ourdata'][1][()]
                   B = self.comparison['cnmf_on_patch']['ourdata'][1]
                   A = np.linalg.norm(A-B)/np.linalg.norm(A)
                   A=A+C
                   B = A < self.comparison['cnmf_on_patch']['sensibility']
                   self.information['values']['cnmf_on_patch'].update({'isdifferent':B,
                                            'diff_data': A,
                                            'diff_timing': data['values']['cnmf_on_patch']['timer']
                                            - self.comparison['cnmf_on_patch']['timer']
                                        
                                })
        #for cnmf full frame
                   A= data['values']['cnmf_full_frame']['ourdata'][0][()]
                   B = self.comparison['cnmf_full_frame']['ourdata'][0]
                   C = np.linalg.norm(A-B)/np.linalg.norm(A)
                   #there is temporal and spatial
                   A= data['values']['cnmf_full_frame']['ourdata'][1][()]
                   B = self.comparison['cnmf_full_frame']['ourdata'][1]
                   A = np.linalg.norm(A-B)/np.linalg.norm(A)
                   #we add both errors
                   A=A+C
                   B = A < self.comparison['cnmf_full_frame']['sensibility']
                   self.information['values']['cnmf_full_frame'].update({'isdifferent':B,
                                            'diff_data': A,
                                            'diff_timing': data['values']['cnmf_full_frame']['timer']
                                            - self.comparison['cnmf_full_frame']['timer']
                                        
                                })
                  
                #we save with the system date
                   dta='/Users/jeremie/CaImAn/comparison/tests/'
                   dta+=dt
                   dta+='.npz'
                   np.savez(dta, **data)
            
            #if we cannot manage to open it or it doesnt exist:
            except (IOError, OSError) :
                #we save but we explain why there were a problem
                print('we were not able to read the file to compare it')
                dta='/Users/jeremie/CaImAn/comparison/tests/NC'
                dta+=dt
                dta+='.npz'
                np.savez(dta, **self.information)