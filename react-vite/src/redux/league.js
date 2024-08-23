import { isAction } from "redux"

GET_ALL_LEAGUES = '/leagues/GET_ALL_LEAGUES'




//-------------------- ACTIONS --------------------//

export const getAllLeagues = (data) => {
    return {
        type: GET_ALL_LEAGUES,
        payload: data
    }
}












//-------------------- THUNKS --------------------//

export const fetchAllLeagues = () => async (dispatch) => {
    const response = await fetch('/api/leagues');

    if (response.ok) {
        const data = response.json();
        dispatch(getAllLeagues(data))
    }
}





//-------------------- REDUCER --------------------//


const initialState = {
    allLeagues: []
}

const leagueReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_LEAGUES:
            return {...state, allLeagues: action.payload}
    }
    default:
        return state;
}

export default leagueReducer
