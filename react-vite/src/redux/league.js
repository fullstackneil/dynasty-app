const GET_ALL_LEAGUES = '/leagues/GET_ALL_LEAGUES'
const GET_SINGLE_LEAGUE = '/leagues/GET_SINGLE_LEAGUE'
const CREATE_LEAGUE = '/leagues/CREATE_LEAGUE'
const EDIT_LEAGUE = '/leagues/EDIT_LEAGUE'
const DELETE_LEAGUE = '/leagues/DELETE_LEAGUE'


//-------------------- ACTIONS --------------------//

export const getAllLeagues = (data) => {
    return {
        type: GET_ALL_LEAGUES,
        payload: data
    }
}

export const getSingleLeague = (data) => {
    return {
        type: GET_SINGLE_LEAGUE,
        payload: data
    }
}

export const createLeague = (data) => {
    return {
        type: CREATE_LEAGUE,
        payload: data
    }
}

export const editLeague = (data) => {
    return {
        type: EDIT_LEAGUE,
        payload: data
    }
}

export const deleteLeague = (data) => {
    return {
        type: DELETE_LEAGUE,
        payload: data
    }
}

//-------------------- THUNKS --------------------//

export const fetchAllLeagues = () => async (dispatch) => {
    const response = await fetch('/api/leagues');

    if (response.ok) {
        const data = await response.json();
        dispatch(getAllLeagues(data))
    }
}

export const fetchSingleLeague = (id) => async (dispatch) => {
    const response = await fetch(`/api/leagues/${id}`)

    if (response.ok) {
        const data = await response.json();
        dispatch(getSingleLeague(data))
        return data;
    }
}

export const createALeague = (newLeague) => async (dispatch) => {
    const response = await fetch('/api/leagues/new', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newLeague),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(createLeague(data))
        return data;
    }
}

export const updateLeague = (newLeague, leagueId) => async (dispatch) => {
    const response = await fetch(`/api/leagues/${leagueId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newLeague)
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(editLeague(data));
        return data;
    }
}

export const deleteALeague = (leagueId) => async (dispatch) => {
    const response = await fetch(`api/leagues/${leagueId}` ,{
        method: 'DELETE'
    })

    if (response.ok) {
        dispatch(deleteLeague(leagueId)); //dispatch leagueId directly
    }
}


//-------------------- REDUCER --------------------//


const initialState = {
    allLeaguesArr: [],
    singleLeague: {},
    createLeague: {},
    editLeague: {},
}

const leagueReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_LEAGUES:
            return {...state, allLeaguesArr: action.payload}
        case GET_SINGLE_LEAGUE:
            return {...state, singleLeague: action.payload}
        case CREATE_LEAGUE:
            return {...state, allLeaguesArr: [...state.allLeaguesArr, action.payload]}
        case EDIT_LEAGUE:
            return {
				...state,
				allLeaguesArr: state.allLeaguesArr.map((league) =>
					league.id === action.payload.id ? action.payload : league
				),
			};
        case DELETE_LEAGUE:{
            return {
                ...state,
                allLeaguesArr: state.allLeaguesArr.filter((league) => league.id !== action.payload)
            };
        }
        default:
            return state;
    }
};

export default leagueReducer
