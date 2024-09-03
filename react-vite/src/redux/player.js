const GET_ALL_PLAYERS = '/players/GET_ALL_LEAGUES'
const GET_SINGLE_PLAYER = '/players/GET_SINGLE_PLAYER'
const CREATE_PLAYER = '/players/CREATE_PLAYER'
const EDIT_PLAYER = '/players/EDIT_PLAYER'
const DELETE_PLAYER = '/players/DELETE_PLAYER'


//-------------------- ACTIONS --------------------//


export const getAllPlayers = (data) => {
    return {
        type: GET_ALL_PLAYERS,
        payload: data
    }
}

export const getSinglePlayer = (data) => {
    return {
        type: GET_SINGLE_PLAYER,
        payload: data
    }
}

export const createPlayer = (data) => {
    return {
        type: CREATE_PLAYER,
        payload: data
    }
}

export const editPlayer = (data) => {
    return {
        type: EDIT_PLAYER,
        payload: data
    }
}

export const deletePlayer = (data) => {
    return {
        type: DELETE_PLAYER,
        payload: data
    }
}

//-------------------- THUNKS --------------------//

export const fetchAllPlayers = () => async (dispatch) => {
    const response = await fetch('/api/players');

    if (response.ok) {
        const data = await response.json();
        dispatch(getAllPlayers(data))
    }
}


//-------------------- REDUCER --------------------//

const initialState = {
    allPlayersArr: []
}

const playerReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_PLAYERS:
            return {...state, allPlayersArr: action.payload}

        default:
            return state;
    }
};

export default playerReducer
