import {
    UPLOAD_PAPERS
} from '../constants/actionTypes'

export default (state = {}, action) => {
    switch (action.type) {
        case UPLOAD_PAPERS:
            return {
                ...state,
                // papers: action.payload.papers
            }
        default:
            return state
    }
}