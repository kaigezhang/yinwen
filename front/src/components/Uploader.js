import Dropzone from 'react-dropzone'
import React from 'react'
import { connect } from 'react-redux'
import {UPLOAD_PAPERS} from "../constants/actionTypes";
import agent from '../agent'

const mapDispatchToProps = dispatch => ({
    onDrop: (files) => dispatch({
        type: UPLOAD_PAPERS,
        files
    })
})

const Uploader = props => {
    const onDrop = (files) => {
        console.log(files)
        let req = agent.Papers.upload()
        files.forEach(file => {
            req.attach('file', file)
        })
        props.onDrop(req.then(res => res.body))
    }

    return (
        <section>
            <div className="dropzone">
                <Dropzone onDrop={onDrop}>
                    <p>批量上传文献</p>
                </Dropzone>
            </div>
        </section>
    )
}

export default connect(null, mapDispatchToProps)(Uploader)