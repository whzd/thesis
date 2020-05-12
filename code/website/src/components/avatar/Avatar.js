import React, { Component } from 'react';
import mock from '../../assets/imgs/mock_avatar.png';

class Avatar extends Component {

    render() {

        const isShown = this.props.show;
        let img;

        if(isShown!=null) {
            img = <div className="mock"><img src={ mock } width="308" height="455"/></div>
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
