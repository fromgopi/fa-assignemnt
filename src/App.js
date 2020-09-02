import React, { Component } from 'react';
import { createBrowserHistory } from 'history';
import { Router, Route } from 'react-router-dom';
import Home from './components/Home';
import Header from './components/layouts/Header';

class App extends Component {
    render() {
        const history = createBrowserHistory();
        return (
            <Router history={history}>
                <Header />
                <Route exact={true} path="/" component={Home}/>
            </Router>
        );
    }
}

export default App;