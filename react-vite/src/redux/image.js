
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
    const response = await fetch(`/images/new`, {
      method: "POST",
      body: post
    });

    if (response.ok) {
        const { resPost } = await response.json();
        dispatch(addPost(resPost));
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
    }
    return state
};

export default imageReducer
