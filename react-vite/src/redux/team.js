const GET_ALL_TEAMS = '/teams/GET_ALL_TEAMS'
const GET_SINGLE_TEAM = '/teams/GET_SINGLE_TEAM'
const GET_ALL_TEAMS_FOR_LEAGUE = '/teams/GET_ALL_TEAMS_FOR_LEAGUE'
const CREATE_TEAM = '/teams/CREATE_TEAM'
const EDIT_TEAM = '/teams/EDIT_TEAM'
const DELETE_TEAM = '/teams/DELETE_TEAM'


//-------------------- ACTIONS --------------------//

export const getAllTeams = (data) => {
    return {
        type: GET_ALL_TEAMS,
        payload: data
    }
}

export const getSingleTeam = (data) => {
    return {
        type: GET_SINGLE_TEAM,
        payload: data
    }
}

export const getTeamsforLeague = (data) => {
    return {
        type: GET_ALL_TEAMS_FOR_LEAGUE,
        payload: data
    }
}

export const createTeam = (data) => {
    return {
        type: CREATE_TEAM,
        payload: data
    }
}

export const editTeam = (data) => {
    return {
        type: EDIT_TEAM,
        payload: data
    }
}

export const deleteTeam = (data) => {
    return {
        type: DELETE_TEAM,
        payload: data
    }
}

//-------------------- THUNKS --------------------//

export const fetchAllTeams = () => async (dispatch) => {
    const response = await fetch('/api/teams');

    if (response.ok) {
        const data = await response.json();
        dispatch(getAllTeams(data))
    }
}

export const fetchAllTeamsforLeague = (league_id) => async (dispatch) => {
    const response = await fetch(`/api/leagues/${league_id}/teams`);

    if (response.ok) {
        const data = await response.json();
        dispatch(getTeamsforLeague(data))
    }
}

export const fetchSingleTeam = (team_id) => async (dispatch) => {
    const response = await fetch(`/api/teams/${team_id}`)

    if (response.ok) {
        const data = await response.json();
        dispatch(getSingleTeam(data))
    }
}

export const createATeam = (user_id, newTeam) => async (dispatch) => {
    const response = await fetch(`/api/${user_id}/teams/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTeam),
    });

    if (response.ok) {
        data = await request.json();
        dispatch(createTeam(data))
        return data
    }
}

export const updateTeam = (team_id, newTeam) => async (dispatch) => {
    const response = await fetch(`/api/teams/${team_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTeam),
    })

    if (response.ok) {
        data = await request.json();
        dispatch(editTeam(data))
        return data
    }
}

export const deleteATeam = (team_id) => async (dispatch) => {
    const response = await fetch(`/api/teams/${team_id}`, {
        methods: 'DELETE'
    })

    if (response.ok) {
        dispatch(deleteTeam(team_id))
    }
}

//-------------------- REDUCER --------------------//


const initialState = {
    allTeamsArr: [],
    singleTeam: {},
    createTeam: {},
    editTeam: {},
}

const teamReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_ALL_TEAMS:
            return {...state, allTeamsArr: action.payload}
        case GET_SINGLE_TEAM:
            return {...state, singleTeam: action.payload}
        case GET_ALL_TEAMS_FOR_LEAGUE:
            return {...state, allTeamsArr: action.payload}
        case CREATE_TEAM:
            return {...state, allTeamsArr: [...state.allTeamsArr, action.payload]}
        case EDIT_TEAM:
            return {
				...state,
				allTeamsArr: state.allTeamsArr.map((team) =>
					team.id === action.payload.id ? action.payload : team
				),
			};
        case DELETE_TEAM:
            const newState = {...state}
            //target the team to be deleted
            delete state.allTeamsArr.find((team) => team.id === action.payload.id)
            return newState;
        default:
            return state;
    }
}

export default teamReducer
