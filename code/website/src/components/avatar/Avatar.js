import React, { Component } from 'react';
import mock from '../../assets/imgs/mock_avatar.png';
import './Avatar.css';

class Avatar extends Component {

    render() {

        if(this.props.show) {
            var img = <div className="mock"><img src={ mock } alt="Mock avatar"/></div>
        }
        else{
            var img = ""
        }

        return (
            <div className="Avatar">
            {img}
            </div>
        )
    }
}

export default Avatar;
