# bookmarked-frontend
## Setting up project locally
1. Make sure node.js is installed         - https://nodejs.org/en/download
2. Change into the frontend directory     - `cd bookmarked-frontend`
3. Download project dependencies          - `npm i`
4. Start development server               - `npm run dev`
5. View the project running on port 5173  - `http://localhost:5173`

## Todo
Add pages for each boundary class extracted from the [analysis document](https://docs.google.com/document/d/142nzC9YF9G2kjyOhJ2z9PXtlsjHaZIlJIsM1bei7F_Q/edit?tab=t.0), and control classes/methods that should be included on the frontend



- [ ] HomePage
    - [ ] NavBar

- [ ] LoginPage
    - [ ] RegistrationForm (component within the page)

- [ ] UserProfilePage 
    - [ ] AccountController
    - [ ] FollowButton 
    - [ ] FollowerListView
    - [ ] SocialController

- [ ] ProfileSettingsPage
    - [ ] SecuritySettingsPage
    - [ ] ProfileEditorForm
    - [ ] ProfileController
    - [ ] AccountSettingsController

- [ ] AdminDashboard
    - [ ] UserManagementPanel (component within dashboard)
    - [ ] PermissionManager
    - [ ] ReviewManger
    - [ ] BookEntryForm
    - [ ] BookController 
    - [ ] BookValidationService 

- [ ] ForumPage
    - [ ] ForumController
    - [ ] DiscussionManager (?)

- [ ] BookDetailPage
    - [ ] BookmarkButton
    - [ ] BookmarkController
    - [ ] RatingWidget
        - [ ] RatingController

- [ ] BookBrowserPage
    - [ ] FilterPanel
    - [ ] ResultsDisplay
    - [ ] BookSearchController

- [ ] ReadingListView
    - [ ] BookShelfManager (? does this differ from bookmark controller)

- [ ] ReviewPage
    - [ ] ReviewForm
    - [ ] ReviewEditor
    - [ ] ReviewController
    - [ ] CommentSection
        - [ ] Confirmation dialog
        - [ ] CommentModerationPanel (admin only)
        - [ ] CommentModerationController
        - [ ] CommentController

- [ ] GoalsPage
    - [ ] GoalEntryForm
    - [ ] GoalController
    - [ ] ProgressTracker

- [ ] ActivityFeedPage
    - [ ] ActivityManager

- [ ] ListsPage 
    - [ ] CreateListForm 
    - [ ] ListController 
    - [ ] ReadingListManager 

- [ ] MyBooksPage
    - [ ] ReadingStatusPanel 
        - [ ] ReadingStatusController
        - [ ] ProgressController
