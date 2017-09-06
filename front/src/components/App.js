import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Uploader from "./Uploader";

class App extends React.Component {
    render () {
        return (
            <div>
                <Switch>
                    <Route path="/upload" component={Uploader}></Route>
                </Switch>
            </div>
        )
    }
}

export default App