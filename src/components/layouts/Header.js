import React, { Component } from 'react';

class Header extends Component {
    render() {
        return (
            <div className="ui inverted menu" style={{ borderRadius: '1px', backgroundColor: '#FF0000'}}>
                <a className='header item'>TodoCRUD</a>
                <a className='item'>Home</a>
            </div>
        );
    }
}

export default Header;