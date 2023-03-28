import { Routes, Route, Link } from "react-router-dom";
import UserPage from "./features/user/UserPage";
import OrganizationPage from "./features/organization/OrganizationPage";
import ProjectPage from "./features/project/ProjectPage";
import TaskPage from "./features/task/TaskPage";
import CommentPage from "./features/comment/CommentPage";
import TagPage from "./features/tag/TagPage";
import InvoicePage from "./features/invoice/InvoicePage";
import PaymentPage from "./features/payment/PaymentPage";
import NotificationPage from "./features/notification/NotificationPage";
import WebhookPage from "./features/webhook/WebhookPage";
import ApiKeyPage from "./features/api_key/ApiKeyPage";
import AuditLogPage from "./features/audit_log/AuditLogPage";

export default function App() {
  return (
    <div>
      <nav>
          <Link to="/users">user</Link>
          <Link to="/organizations">organization</Link>
          <Link to="/projects">project</Link>
          <Link to="/tasks">task</Link>
          <Link to="/comments">comment</Link>
          <Link to="/tags">tag</Link>
          <Link to="/invoices">invoice</Link>
          <Link to="/payments">payment</Link>
          <Link to="/notifications">notification</Link>
          <Link to="/webhooks">webhook</Link>
          <Link to="/api_keys">api_key</Link>
          <Link to="/audit_logs">audit_log</Link>
      </nav>
      <main>
        <Routes>
        <Route path="/users" element={<UserPage />} />
        <Route path="/organizations" element={<OrganizationPage />} />
        <Route path="/projects" element={<ProjectPage />} />
        <Route path="/tasks" element={<TaskPage />} />
        <Route path="/comments" element={<CommentPage />} />
        <Route path="/tags" element={<TagPage />} />
        <Route path="/invoices" element={<InvoicePage />} />
        <Route path="/payments" element={<PaymentPage />} />
        <Route path="/notifications" element={<NotificationPage />} />
        <Route path="/webhooks" element={<WebhookPage />} />
        <Route path="/api_keys" element={<ApiKeyPage />} />
        <Route path="/audit_logs" element={<AuditLogPage />} />
        </Routes>
      </main>
    </div>
  );
}
