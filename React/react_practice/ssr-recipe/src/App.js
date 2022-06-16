import React from "react";
import { Route, Routes } from "react-router-dom";
import Menu from "./components/Menu";
import RedPage from "./pages/RedPage";
import BluePage from "./pages/BluePage";
import UsersPage from "./pages/UsersPage";

function App() {
    return (
        <>
            <Menu />
            <hr />
            <Routes>
                <Route path="/" element={<Menu />} />
                <Route path="/undefined" element={<Menu />} />
                <Route path="/red" element={<RedPage />} />
                <Route path="/blue" element={<BluePage />} />
                <Route path="/users" element={<UsersPage />} />
            </Routes>
        </>
    );
}

export default App;
