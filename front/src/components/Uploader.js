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

class Uploader extends React.Component {
    constructor () {
        super()
        this.state = {
            files: []
        }
        this.onDrop = files => {
            this.setState({
                files
            })
            agent.Papers.upload(files)
        }
    }

    render () {
        return (
            <section>
                <div className="dropzone">
                    <Dropzone onDrop={this.onDrop}>
                        <p>批量上传文献</p>
                    </Dropzone>
                </div>
                <aside>
                    <h2>需要上传的文件</h2>
                    <ul>
                        {
                            this.state.files.map(
                                f => <li key={f.name}>{f.name} -- {f.size}</li>
                            )
                        }
                    </ul>
                </aside>
            </section>
        )

    }
}


export default connect(null, mapDispatchToProps)(Uploader)