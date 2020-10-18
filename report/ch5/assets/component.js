class Avatar extends Component {
    render() {
        const isShown = this.props.show;
        let img;
        if(isShown!=null) {
            img = <div className="mock"><img src={ mock } alt="Mock avatar"/></div>
        }
        else{img = ""}
        return (
            <div className="Avatar">
                {img}
            </div>
        )
    }
}
