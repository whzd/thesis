import React, { Component } from 'react';
import mock from '../../assets/imgs/mock_avatar.png';

class Avatar extends Component {

    render() {

        const isShown = this.props.show;
        let img;

        if(isShown) {
            img = <div className="mock"><img src={ mock } width="308" height="455"/></div>
        }

        return (
            <div className="Avatar">
            Avatar block
            {img}
            </div>
        )
    }
}

export default Avatar;
