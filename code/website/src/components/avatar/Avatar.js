import React, { Component } from 'react';
import mock from '../../assets/imgs/mock_avatar.png';
import './Avatar.css';

class Avatar extends Component {

    render() {

        const isShown = this.props.show;
        let img;

        if(isShown!=null) {
            img = <div className="mock"><img src={ mock } /></div>
        }
        else{
            img = ""
        }

        return (
            <div className="Avatar">
            {img}
            </div>
        )
    }
}

export default Avatar;
