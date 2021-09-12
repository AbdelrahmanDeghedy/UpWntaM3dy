import { createStore } from 'vuex';
import { stateType } from './interfaces';

import { mutations } from './mutations';


export const store = createStore({
    state () : stateType {
        return {
            users : [],
            answers : [],
            questions : [],
            courseInfoPerTerm : []
        }
    },
    mutations,
    
})
 
