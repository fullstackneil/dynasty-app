
const ADD_POST = '/images/ADD_POST'

//ACTION

export const addPost = (data) => {
    return {
        type: ADD_POST,
        payload: data
    }
}



//THUNKS

export const createPost = (post) => async (dispatch) => {
    console.log('IN CREATE IMAGE THUNK')
    const response = await fetch(`/api/images/new`, {
      method: "POST",
      body: post
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(addPost(data.image));
        return data.image;
    } else {
        console.log("There was an error making your post!")
    }
};


//REDUCER

const initialState = {
    addPost: []
}

const imageReducer = (state = initialState, action) => {
    switch (action.type) {
        case ADD_POST:
            return {...state, addPost: action.payload}
    default:
        return state
    }
};

export default imageReducer
